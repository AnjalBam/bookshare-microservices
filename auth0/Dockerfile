FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app/auth0

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . ./