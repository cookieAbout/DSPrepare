FROM ubuntu:latest
LABEL authors="Svetlana"
# -y - да по умолчанию
RUN apt-get update && apt-get install -y vim wget curl git

WORKDIR /home/svpanchenko
# мой комп -> контейнер
COPY ./test_loop_script.py ./test_loop_script.py

RUN touch hello.sh && echo "echo 'Hello from container'" > hello.sh

ENTRYPOINT ["top", "-b"]

#CMD ["top"]