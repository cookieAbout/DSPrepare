from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

open_ai = OpenAI(temperature=0.3)


template = """
Роль: дружелюбный telegram бот-флорист.
На вход получаешь: клиентское описание цветка.
Задача: подобрать 3 цветка максимально похожие по описанию {user_query}.
Приветствовать не нужно, это сделано ранее. Выдать только строку с названиями цветов и вопрос, угадал ли ты то,
что хочет пользователь.
"""
# пример чтения из интернета
# https://floris22.ru/about-company/blog/projects/advise/cvety-pohozhie-na-romashki.html#zagolovok4


async def llm_chain(message: str):
    prompt = PromptTemplate(
        input_variables=["user_query"], template=template
    )
    chain = (prompt | open_ai)
    answer = chain.invoke({'user_query': message})
    return answer
