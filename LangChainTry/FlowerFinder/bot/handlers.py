from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from LLM.llm_florist import LLMAgent
from bot.keyboards import get_main_keyboard


# from database.session import get_db


class DescriptionState(StatesGroup):
    waiting_for_description = State()


async def cmd_start(message: types.Message):
    """ Обработчик команды start """
    await message.answer("Привет! Я помогу тебе подобрать цветы для любимого человека, если ты забыл название.",
                         reply_markup=get_main_keyboard()
                         )


async def cmd_help(message: types.Message):
    """ Обработчик команды ℹ️ Помощь """
    help_text = """
    Доступные команды:
    /start - Начать работу с ботом
    /help - Показать справку
    /history - вспомнить, что уже спрашивал
    /clear - очистить историю вопросов
    /not_found - завершить, если цветок так и не найден (запросы будут обработаны в будущем)
    """
    await message.answer(help_text, reply_markup=get_main_keyboard())


async def cmd_add_descriptions(message: types.Message):
    await DescriptionState.waiting_for_description.set()
    await message.answer("Ввести описание цветка:")


async def cmd_llm_answer(message: types.Message, state: FSMContext):
    """ Обработчик команды 🔍 Ввести описание цветка """
    agent = LLMAgent()
    try:
        response = await agent.get_llm_answer(message.text)
        await message.answer(response.content, reply_markup=get_main_keyboard())
    except Exception as e:
        await message.answer(f"Ошибка: {e}")

    await state.finish()


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


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])
    dp.register_message_handler(cmd_help, lambda msg: msg.text == "ℹ️ Помощь")
    dp.register_message_handler(cmd_add_descriptions, lambda msg: msg.text == "🔍 Ввести описание цветка")
    dp.register_message_handler(cmd_llm_answer, state=DescriptionState.waiting_for_description)
    # dp.register_message_handler(cmd_history, commands=["history"])
    # dp.register_message_handler(cmd_clear, commands=["clear"])
    # dp.register_message_handler(cmd_not_found, commands=["not_found"])
