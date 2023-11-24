FROM python:3.11.6-slim-bookworm

ENV APP_HOME=/app

RUN mkdir -p $APP_HOME
RUN mkdir -p $APP_HOME/staticfiles
RUN mkdir -p $APP_HOME/mediafiles

WORKDIR $APP_HOME

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod +rx entrypoint-web.sh
RUN chmod +rx entrypoint-celery.sh
