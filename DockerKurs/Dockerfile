#FROM ubuntu:22.04
#WORKDIR /home
#RUN mkdir -p /home/user/app
#COPY script.sh /home/user/app/script.sh
#CMD ["bash", "/home/user/app/script.sh"]

#FROM ubuntu:22.04
#COPY script.sh script.sh
#ENTRYPOINT ["bash", "script.sh"]
#CMD ["world"]


#FROM ubuntu:jammy
#
#WORKDIR /app
#
#RUN apt-get update && apt-get install -y vim wget curl git
#RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.2.1/zsh-in-docker.sh)" -- \
#    -t robbyrussell \
#    -p https://github.com/zsh-users/zsh-autosuggestions
#
#ENV ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=#dedede,bg=#9c9c9c,bold,underline"
#
#COPY script.sh script.sh
#
#ENTRYPOINT ["zsh"]
#CMD ["script.sh"]



#FROM ubuntu:jammy
#
#WORKDIR /app
#
#COPY script.sh script.sh
#
#ENTRYPOINT ["/bin/bash", "script.sh"]

#FROM python:3.8
#
#RUN echo "Start build"
#
#RUN python -m pip install --upgrade pip \
#    && pip install click==8.1.2 \
#    && pip install Flask==2.1.1 \
#    && pip install Flask-Cors==3.0.10 \
#    && pip install Flask-SQLAlchemy==2.5.1 \
#    && pip install greenlet==1.1.2 \
#    && pip install gunicorn==20.1.0 \
#    && pip install importlib-metadata==4.11.3 \
#    && pip install itsdangerous==2.1.2 \
#    && pip install Jinja2==3.1.1 \
#    && pip install MarkupSafe==2.1.1 \
#    && pip install psycopg2-binary==2.9.3 \
#    && pip install six==1.16.0 \
#    && pip install SQLAlchemy==1.4.34 \
#    && pip install Werkzeug==2.1.0 \
#    && pip install zipp==3.7.0
#
#COPY ./app.py /src/app.py
### точка входа в контейнер
#ENTRYPOINT ["python3", "app.py"]

#FROM ubuntu:22.04
#WORKDIR /app
#COPY script.sh script.sh
#COPY names.txt names.txt
#ENTRYPOINT ["bash", "script.sh"]

FROM python:3.10
WORKDIR /app
COPY script.py script.py
ENTRYPOINT ["python", "-u", "script.py"]
