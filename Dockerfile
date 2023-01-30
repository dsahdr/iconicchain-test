FROM python:3.11

ENV PYTHONUNBUFFERED=1

RUN mkdir /code
WORKDIR /code

RUN apt-get update && apt-get install -y netcat
RUN pip install --upgrade pip

COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY . /code/

COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh

COPY ./start /start
RUN chmod +x /start


ENTRYPOINT ["/entrypoint.sh"]
