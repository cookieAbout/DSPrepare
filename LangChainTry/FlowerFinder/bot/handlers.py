from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from LLM.llm_florist import LLMAgent
from bot.keyboards import get_main_keyboard


# from database.session import get_db


class DescriptionState(StatesGroup):
    waiting_for_description = State()
    confirming = State()


async def cmd_start(message: types.Message):
    """ Обработчик команды start """
    await DescriptionState.waiting_for_description.set()
    await message.answer("""
Привет! Я помогу тебе подобрать цветы для любимого человека, если ты забыл название.
Опиши, пожалуйста, как выглядит цветок, который ты ищешь:
""", reply_markup=get_main_keyboard())


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
    await message.answer(help_text)


async def cmd_llm_answer(message: types.Message):
    """ Обработчик ввода описания цветка """
    agent = LLMAgent()
    try:
        await types.ChatActions.typing()  # Отображается состояние печати
        response = await agent.get_llm_answer(message.text)
        await DescriptionState.confirming.set()
        await message.answer(response.content)
        # await message.reply_photo(photo=agent.get_flower_picture(response.content))
    except Exception as e:
        await message.answer(f"Произошла ошибка при обработке запроса: {str(e)}")
        await DescriptionState.waiting_for_description.set()


async def cmd_confirm_description(message: types.Message, state: FSMContext):
    """ Обработчик подтверждения или отклонения результата """
    if message.text == "Да, то что нужно!":
        await message.answer(f"Всегда рад помочь!")
        await state.finish()
    elif message.text == "Не то":
        await DescriptionState.waiting_for_description.set()
        await message.answer("Попробуйте уточнить описание цветка:")
    elif message.text == "Так и не нашел. Выйти.":
        await message.answer("Я сохраню ваш запрос и подумаю позже")
        await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])
    dp.register_message_handler(cmd_help, lambda msg: msg.text == "ℹ️ Помощь")
    dp.register_message_handler(
        cmd_llm_answer, state=DescriptionState.waiting_for_description, content_types=types.ContentTypes.TEXT
    )
    dp.register_message_handler(
        cmd_confirm_description,
        lambda msg: msg.text in ['Да, то что нужно!', 'Не то', 'Так и не нашел. Выйти.'],
        state=DescriptionState.confirming
    )
