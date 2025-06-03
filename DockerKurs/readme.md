Создание image из папки с Dockerfile 

    docker build . -t name_lower_case
    docker build -t name_lower_case -f HeadPath/Path/Dockerfile .  # установка с зависимостями из других файлов

Запуск контейнера

    docker run name_lower_case