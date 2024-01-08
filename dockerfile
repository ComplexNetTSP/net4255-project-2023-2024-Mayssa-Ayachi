# syntax=docker/dockerfile:1

FROM python:3-alpine

WORKDIR /app

COPY . .

RUN pip install Flask


EXPOSE 5000

CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]