## -- Чат-бот для ВКонтакте --

### Общее описание
>Чат-бот для ВКонтакте, который функционирует как витрина выпечки или кондитерских изделий. 
Бот взаимодействует с пользователем через сообщения сообщества, используя официальное API ВКонтакте 
и подключение через Long Poll сервер.

### Реализован следующий функционал
 - Для каждого товара предусмотрено краткое описание с фотографией
 - Навигация реализована с помощью кнопок
 - Пользователь может перемещаться по категориям
 - Данные хранятся в БД sqlite
 - Реализована машина состояний при помощи библиотеки transitions
 - Реализован запуск проекта в Docker контейнере
 - Реализованы тесты основног функционала бота на Pytest

### Установка и запуск 
#### Для запуска проекта на локальном компьтере в контейнере:
- Cклонируйте репозиторий в рабочую папку:
  ```shell
  git clone git@github.com:PetrovKRS/VKBot_DEF_Company.git
  ```
- Установите docker compose
  ```shell
  sudo apt update
  sudo apt install curl
  curl -fsSL https://get.docker.com -o get-docker.sh
  sudo sh get-docker.sh
  sudo apt install docker-compose
  ```
- Перейдите в корневую папку склонированного репозитория:
- Создайте в корне проекта .env файл и заполните его следующими данными (см. env_example.txt):
  ```
    VK_GROUP_TOKEN = '<your_vk_group_token>'
    VK_GROUP_ID = '<your_vk_group_id>'
    DB_URL = 'sqlite:///data/vk_bot.db'
  ```
- Создайте виртуальное окружение:
  ```shell    
  python3 -m venv venv
  source venv/bin/activate
  ```
- Установите зависимости:
  ```shell
  pip install --upgrade pip
  pip install -r requirements.txt
  ```
- Запустите проект в docker контейнерах
  ```shell
  sudo docker compose up --build
  ```
- Запустить в контейнере скрипт создания БД и заполнения тестовыми данными:
  ```shell
  sudo docker compose exec vk_bot chmod +x start.sh
  sudo docker compose exec vk_bot ./start.sh
  ```
- Для начала работы с ботом отправьте ему команду:
  ```
  Начать
  ```
  
### В проекте реализованы следующие тесты:
- Тест CRUD операций с базой данных.
- Тест отправки сообщений через API.
- Тест работы машины состояний.
- Тест обработки команды "Начать" (команда для начала работы с ботом)
##### для запуска тестов с указанием процента покрытия
  ```shell
  pytest --cov -vv
  ```

***

### <b> Стек технологий: </b>

![Python](https://img.shields.io/badge/-Python_3.12-df?style=for-the-badge&logo=Python&labelColor=yellow&color=blue)
![DOCKER](https://img.shields.io/badge/-DOCKER-df?style=for-the-badge&logo=DOCKER&labelColor=black&color=blue)
![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-df?style=for-the-badge&logo=SQLAlchemy&labelColor=black&color=blue)
![Transitions](https://img.shields.io/badge/-Transitions-df?style=for-the-badge&logo=Transitions&labelColor=lightblue&color=blue)
![VK](https://img.shields.io/badge/-VK_API-df?style=for-the-badge&logo=VK_API&labelColor=lightblue&color=blue)
![Pytest](https://img.shields.io/badge/-Pytest-df?style=for-the-badge&logo=Pytest&labelColor=black&color=blue)
![SQLite](https://img.shields.io/badge/-SQLite-df?style=for-the-badge&logo=SQLite&labelColor=black&color=blue)

***
### Автор проекта: 
[![GitHub](https://img.shields.io/badge/-Андрей_Петров-df?style=for-the-badge&logo=GitHub&labelColor=black&color=blue)](https://github.com/PetrovKRS)
***
