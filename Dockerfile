# Используем Python-образ как основу
FROM python:3.12-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы приложения в контейнер
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем переменные окружения (можно переопределить через Docker Compose)
ENV VK_GROUP_TOKEN=<your_vk_group_token>
ENV VK_GROUP_ID=<your_vk_group_id>

# Команда для запуска бота
CMD ["python3", "bot.py"]
