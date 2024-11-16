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
 - реализована машина состояний при помощи библиотеки transitions

### Установка и запуск 
### Для запуска проекта на локальном компьтере в контейнерах:
- Cклонируйте репозиторий в рабочую папку:
  ```
  git clone git@github.com:PetrovKRS/VKBot_DEF_Company.git
  ```
- Создайте в корне проекта .env файл и заполните его следующими данными (см. env_example.txt):
  ```
    VK_GROUP_TOKEN = '<your_vk_group_token>'
    VK_GROUP_ID = '<your_vk_group_id>'
    DB_URL = 'sqlite:///data/vk_bot.db'
  ```

- Установите docker compose
  ```
  sudo apt update
  sudo apt install curl
  curl -fsSL https://get.docker.com -o get-docker.sh
  sudo sh get-docker.sh
  sudo apt install docker-compose
  ```
- Перейдите в корневую папку склонированного репозитория:
- Запустите проект в docker контейнерах
  ```
  sudo docker compose up --build
  ```
- Для начала работы с ботом введите команду:
  ```
  Начать
  ```


### <b> Стек технологий: </b>

![Python](https://img.shields.io/badge/-Python_3.12-df?style=for-the-badge&logo=Python&labelColor=yellow&color=blue)
![DOCKER](https://img.shields.io/badge/-DOCKER-df?style=for-the-badge&logo=DOCKER&labelColor=lightblue&color=blue)
![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-df?style=for-the-badge&logo=SQLAlchemy&labelColor=black&color=blue)
![Transitions](https://img.shields.io/badge/-Transitions-df?style=for-the-badge&logo=Transitions&labelColor=lightblue&color=blue)
![VK_API](https://img.shields.io/badge/-VK_API-df?style=for-the-badge&logo=VK_API&labelColor=lightblue&color=blue)
### Технологии
- Python
- vk_api
- DOCKER
- SQLAlchemy
- transitions

