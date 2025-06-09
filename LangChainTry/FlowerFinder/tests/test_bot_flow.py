import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from aiogram import types
from FlowerFinder.bot.handlers import (
    # cmd_start,
    cmd_llm_answer,
    # cmd_confirm_description,
    # DescriptionState
)


class TestBotFlow:
    @pytest.fixture
    def message(self):
        """Фикстура для создания тестового сообщения"""
        message = AsyncMock(spec=types.Message)
        message.text = "test message"
        message.answer = AsyncMock()
        return message

    @pytest.fixture
    def state(self):
        """Фикстура для создания тестового состояния"""
        state = AsyncMock()
        state.set_state = AsyncMock()
        state.finish = AsyncMock()
        return state

    # @pytest.mark.asyncio
    # async def test_cmd_start(self, message, state):
    #     """Тест команды старта бота"""
    #     await cmd_start(message)
    #
    #     # Проверяем, что бот отправил приветственное сообщение
    #     message.answer.assert_called_with(
    #         "Привет! Я помогу тебе подобрать цветы для любимого человека, если ты забыл название."
    #     )
    #
    #     # Проверяем, что бот перешел в состояние ожидания описания
    #     assert message.answer.call_count == 2
    #     message.answer.assert_called_with(
    #         "Опиши, пожалуйста, как выглядит цветок, который ты ищешь:"
    #     )

    @pytest.mark.asyncio
    async def test_cmd_llm_answer(self, message):
        """Тест обработки ввода описания цветка"""
        with patch('FlowerFinder.bot.handlers.LLMAgent') as mock_llm:
            mock_agent = MagicMock()
            mock_agent.get_llm_answer_with_memory = AsyncMock(
                return_value=MagicMock(content="Test response")
            )
            mock_llm.return_value = mock_agent

            await cmd_llm_answer(message)

            # Проверяем, что LLM был вызван с правильным текстом
            mock_agent.get_llm_answer_with_memory.assert_called_with("test message")

            # Проверяем, что бот отправил ответ
            message.answer.assert_called_with("Test response")

    # @pytest.mark.asyncio
    # async def test_cmd_confirm_description_yes(self, message, state):
    #     """Тест подтверждения результата"""
    #     message.text = "Да, то что нужно!"
    #     await cmd_confirm_description(message, state)
    #
    #     # Проверяем, что бот отправил сообщение об успехе
    #     message.answer.assert_called_with("Всегда рад помочь!")
    #     # Проверяем, что состояние было завершено
    #     state.finish.assert_called_once()
    #
    # @pytest.mark.asyncio
    # async def test_cmd_confirm_description_no(self, message, state):
    #     """Тест отклонения результата"""
    #     message.text = "Не то"
    #     await cmd_confirm_description(message, state)
    #
    #     # Проверяем, что бот перешел в состояние ожидания уточнения
    #     state.set_state.assert_called_with(DescriptionState.waiting_for_description)
    #     # Проверяем, что бот отправил сообщение с просьбой уточнить описание
    #     message.answer.assert_called_with("Попробуйте уточнить описание цветка:")
    #
    # @pytest.mark.asyncio
    # async def test_cmd_confirm_description_exit(self, message, state):
    #     """Тест выхода из бота"""
    #     message.text = "Так и не нашел. Выйти."
    #     await cmd_confirm_description(message, state)
    #
    #     # Проверяем, что бот отправил сообщение о сохранении запроса
    #     message.answer.assert_called_with("Я сохраню ваш запрос и подумаю позже")
    #     # Проверяем, что состояние было завершено
    #     state.finish.assert_called_once()
