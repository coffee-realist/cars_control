# Базовый образ
FROM python:3.10-slim

# Отключаем байт-код и задаем вывод без буферизации
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости (Git + Python)
RUN apt-get update && apt-get install -y git && apt-get clean && rm -rf /var/lib/apt/lists/*

# Клонируем проект из репозитория
ARG REPO_URL
RUN git clone $REPO_URL /app

# Устанавливаем зависимости Python
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
