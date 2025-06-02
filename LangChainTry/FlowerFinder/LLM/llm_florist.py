from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(temperature=0.9)


template = """
Роль: дружелюбный telegram бот-флорист.
На вход получаешь: клиентское описание цветка.
Задача: подобрать 3 цветка максимально похожие по описанию.
Пример: Цветок, похожий на ромашку, но больше - Анациклюс, Хризантема, Арктотис.
"""
# пример чтения из интернета
# https://floris22.ru/about-company/blog/projects/advise/cvety-pohozhie-na-romashki.html#zagolovok4


async def llm_chain(message: str):
    prompt = PromptTemplate(
        input_variables=["описание цветка"], template=template
    )
    chain = (prompt | llm).as_tool()
    return chain.invoke(message)
