from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain_openai import ChatOpenAI

# пример чтения из интернета
# https://floris22.ru/about-company/blog/projects/advise/cvety-pohozhie-na-romashki.html#zagolovok4


class LLMAgent:
    """ Класс LLM Agent """
    def __init__(self):
        self.temperature = 0.5
        self.system_prompt = SystemMessagePromptTemplate.from_template('''
  Ты - вежливый бот-флорист. Твоя задача подсказать пользователю название цветка по его описанию.
  Поздоровайся. Попроси ввести описание цветка, который он ищет.
  Выведи до трех вариантов наиболее похожих на описание.
  Спроси, есть ли среди названных нужный.
  Если нет, попроси дополнить описание и предложи еще до трех вариантов.
  Повторяй, пока не найдешь нужный или пользователь не попросит остановиться.
        ''')
        self.human_prompt = HumanMessagePromptTemplate.from_template('{user_query}')

    def _get_chat_prompt(self):
        """ Объединяем промпты в шаблон """
        return ChatPromptTemplate.from_messages([self.system_prompt, self.human_prompt])

    def get_llm_answer(self, message: str):
        """ Создаем цепочку """
        llm = ChatOpenAI(temperature=self.temperature)
        prompt = self._get_chat_prompt()
        chain = (prompt | llm)
        return chain.ainvoke({'user_query': message})
