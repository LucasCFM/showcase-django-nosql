FROM python:3.6

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y

RUN apt-get install -y apt-utils

RUN mkdir -p /var/log
RUN mkdir /app
COPY ./src /app

WORKDIR /app

RUN pwd
RUN ls -a

RUN python -m pip install -r requirements/requirements.txt
RUN cd /app \
    && python manage.py migrate

CMD ["sh", "./start.sh"]

EXPOSE 8080