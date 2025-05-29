# Заметки разбора обучающих уроков
http://127.0.0.1:8000/docs#

Важен порядок указания вью - от частного к общему


### poetry
poetry - менеджер зависимостей https://python-poetry.org/

    add - например "uvicorn[standart]", установка конкретных библиотек с нужными зависимостями
    install - установка зависимостей
    install --sync - синхронизация зависимостей, с теми, что установлены
    new - создание проекта
    init - инициализация зависимостей
    show - посмотреть зависимости

alembic - управление миграциями. Сравнивает, что в БД и что мы ожидаем видеть

    alembic init -t async alembic - создаем необходимые связи alembic
    alembic revision -m  "create accounts table" - авто создание таблиц
    alembic revision --autogenerate -m  "create products table" - автогенерация таблиц из python
    alembic upgrade head - обновление до последней миграции
    alembic downgrade -1 - откат последнего, в самое начало откатывает base вместо -1
    alembic history - история миграций
    alembic current - текущая миграция

модуль versions связан с таблицей alembic_version. Если что-то из этого удалить, возникнет конфликт версий
