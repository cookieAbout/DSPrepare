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
        response = await agent.get_llm_answer_with_memory(message.text)
        async with state.proxy() as data:
            data['description'] = message.text
            data['enriched'] = response

        await DescriptionState.confirming.set()
        await message.answer(response.content, reply_markup=get_main_keyboard())
    except Exception as e:
        await message.answer(f"Ошибка: {e}")


async def cmd_confirm_description(message: types.Message, state: FSMContext):
    """ Обработчик выхода из цикла поиска цветка """
    if message.text == "Да, то что нужно!":
        await message.answer(f"Всегда рад помочь!")
        await state.finish()

    else:
        await DescriptionState.waiting_for_description.set()
        await message.answer("Попробуйте перефразировать описание цветка:")


async def cmd_not_found(message: types.Message, state: FSMContext):
    """ Обработчик /not_found """
    await message.answer('Я сохраню описание и подумаю над другими вариантами', reply_markup=get_main_keyboard())
    await state.finish()
    # обработка не найденных


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])
    dp.register_message_handler(cmd_help, lambda msg: msg.text == "ℹ️ Помощь")
    dp.register_message_handler(cmd_add_descriptions, lambda msg: msg.text == "🔍 Ввести описание цветка")
    dp.register_message_handler(cmd_llm_answer, state=DescriptionState.waiting_for_description)
    dp.register_message_handler(
        cmd_confirm_description,
        lambda msg: msg.text in ['Да, то что нужно!', 'Не то'],
        state=DescriptionState.confirming
    )
    dp.register_message_handler(cmd_not_found, lambda msg: msg.text == "Так и не нашел. Выйти.")
