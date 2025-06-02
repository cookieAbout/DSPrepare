from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from FlowerFinder.LLM.llm_florist import llm_chain
# from database.session import get_db


class DescriptionState(StatesGroup):
    waiting_for_description = State()


async def cmd_start(message: types.Message):
    """ Обработчик команды start """
    await message.answer("""
  Привет! Я помогу тебе подобрать цветы для любимого человека, если ты забыл название.
  Введи описание, какой цветок ты ищешь:
  """
                         )


async def cmd_help(message: types.Message):
    """ Обработчик команды help """
    help_text = """
    Доступные команды:
    /start - Начать работу с ботом
    /help - Показать справку
    /enter_description - введи описание
    /history - вспомнить, что уже спрашивал
    /clear - очистить историю вопросов
    /not_found - завершить, если цветок так и не найден (запросы будут обработаны в будущем)
    """
    await message.answer(help_text)


async def cmd_description(message: types.Message, state: FSMContext):
    """ Обработчик /enter_description """
    async with state.proxy() as data:
        data['description'] = message.text
    await DescriptionState.waiting_for_description.set()
    await message.answer('Введите описание цветка, который ищите:')


async def cmd_history(message: types.Message):
    """ Обработчик /history"""
    pass
    # db = next(get_db())
    # histories = get_history(db)
    # if not histories:
    #     await message.answer("Вы пока ничего не спрашивали :(")
    #     return
    # history_list = "\n".join([f"{history.id}." for history in histories])
    # await message.answer(f"Ваши запросы:\n{history_list}")


async def cmd_clear():
    """ Обработчик /clear """
    pass


async def cmd_not_found():
    """ Обработчик /not_found """
    pass


async def chain_flower_query(message: types.Message):
    # 1. Получаем ответ от LLM
    response = llm_chain(message.text)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])
    dp.register_message_handler(cmd_help, commands=["help"])
    dp.register_message_handler(cmd_description, commands=["enter_description"])
    dp.register_message_handler(cmd_history, commands=["history"])
    dp.register_message_handler(cmd_clear, commands=["clear"])
    dp.register_message_handler(cmd_not_found, commands=["not_found"])
