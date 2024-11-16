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

### Установка и запуск 
#### Для запуска проекта на локальном компьтере в контейнерах:
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
- Для начала работы с ботом введите команду:
  ```
  Начать
  ```
***

### <b> Стек технологий: </b>

![Python](https://img.shields.io/badge/-Python_3.12-df?style=for-the-badge&logo=Python&labelColor=yellow&color=blue)
![DOCKER](https://img.shields.io/badge/-DOCKER-df?style=for-the-badge&logo=DOCKER&labelColor=lightblue&color=blue)
![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-df?style=for-the-badge&logo=SQLAlchemy&labelColor=black&color=blue)
![Transitions](https://img.shields.io/badge/-Transitions-df?style=for-the-badge&logo=Transitions&labelColor=lightblue&color=blue)
![VK](https://img.shields.io/badge/-VK_API-df?style=for-the-badge&logo=VK_API&labelColor=lightblue&color=blue)

***
### Автор проекта: 
[![GitHub](https://img.shields.io/badge/-Андрей_Петров-df?style=for-the-badge&logo=GitHub&labelColor=black&color=blue)](https://github.com/PetrovKRS)
***
