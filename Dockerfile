FROM python:3.9-alpine3.13
LABEL maintainer="Nicholas Karimi"

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt


WORKDIR /app

EXPOSE 8000

RUN python -m venv /py && \
	/py/bin/pip install --upgrade pip && \
	apk update && \
	apk add postgresql-dev gcc python3-dev musl-dev && \
    /py/bin/pip install -r /requirements.txt

ENV PATH="/py/bin:$PATH"

