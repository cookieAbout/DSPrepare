# import uuid
import openai
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
from langchain_gigachat import GigaChat
from config import settings

# пример чтения из интернета
# https://floris22.ru/about-company/blog/projects/advise/cvety-pohozhie-na-romashki.html#zagolovok4


class LLMAgent:
    """ Класс LLM Agent """
    def __init__(self):
        self.temperature = 0.7
        self.system_prompt = SystemMessagePromptTemplate.from_template('''
  Ты - вежливый бот-флорист. Твоя задача подсказать пользователю название цветка по его описанию.
  Игнорирую сообщения, не связанные с описанием цветов.
  Выведи только название цветка, максимально похожего по описанию, без лишних слов.
  Выведи сообщением "Это то, что вы искали? (Нажмите кнопку)"
  Продолжай выводить по одному, пока клиент не нажмет "Да, то что нужно!".
        ''')
        self.human_prompt = HumanMessagePromptTemplate.from_template('{user_query}')
        self.session_ids = {}

    def _get_chat_prompt(self):
        """ Объединяем промпты в шаблон """
        return ChatPromptTemplate.from_messages([self.system_prompt, self.human_prompt])

    def get_session_history(self, session_id: str) -> InMemoryChatMessageHistory:
        """ https://python.langchain.com/api_reference/langchain/chains/langchain.chains.conversation.base.ConversationChain.html """
        if session_id not in self.session_ids:
            self.session_ids[session_id] = InMemoryChatMessageHistory()
        return self.session_ids[session_id]

    @staticmethod
    def get_flower_picture(flower_name: str):
        """ Генерация изображения цветка """
        response = openai.images.generate(
            prompt=flower_name,
            n=1,
            size="512x512",
        )
        return response.data[0].url

    def get_chat_open_ai_model(self):
        """"""
        return ChatOpenAI(temperature=self.temperature)

    def get_gigachat_model(self):
        """"""
        return GigaChat(
            credentials=settings.GIGACHAT_API_PERS,
            model="GigaChat-2-Max",
            verify_ssl_certs=False,
            temperature=self.temperature,
        )

    def get_llm_answer(self, message: str):
        """ Создаем цепочку """
        llm = self.get_chat_open_ai_model()
        # llm = self.get_gigachat_model()
        prompt = self._get_chat_prompt()
        chain = (prompt | llm)
        return chain.ainvoke({'user_query': message})

    def get_llm_answer_with_memory(self, message: str):
        """ """
        # llm = self.get_gigachat_model()
        llm = self.get_chat_open_ai_model()
        prompt = self._get_chat_prompt()
        chain = (prompt | llm)
        chain_with_history = RunnableWithMessageHistory(
            chain,
            self.get_session_history,
            input_messages_key="user_query"
        )
        return chain_with_history.ainvoke(
            {'user_query': message},
            config={"configurable": {"session_id": "1"}},  # str(uuid.uuid4())
        )
