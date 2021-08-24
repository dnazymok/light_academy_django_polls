FROM python:3.8-slim

LABEL maintainer="dnazymok@gmail.com"

RUN apt-get update && apt-get install -y\
    build-essential && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["bash", "/app/docker-entrypoint.sh"]