import json
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from database import Session, init_db, seed_data
from models import Category, Product
from states import UserState, create_state_machine
from config import VK_GROUP_TOKEN, VK_GROUP_ID

vk_session = VkApi(token=VK_GROUP_TOKEN)
longpoll = VkBotLongPoll(vk_session, VK_GROUP_ID)
vk = vk_session.get_api()

users = {} # База для хранения состояний пользователей


def send_message(user_id, message, keyboard=None):
    """ Отправка сообщений пользователю. """
    vk.messages.send(
        user_id=user_id,
        message=message,
        random_id=0,
        keyboard=keyboard
    )


def create_keyboard(buttons):
    """ Создание клавиатуры с кнопками """
    return json.dumps(
        {
            'one_time': False,
            'buttons': [
                [
                    {
                        'action': {
                            'type': 'text', 'label': btn
                        }, 'color': 'primary'
                    }
                ] for btn in buttons
            ]
        }
    )


def handle_event(event, msg=None):
    """ Обработка сообщений от пользователей. """
    user_id = event.message['from_id']
    message = event.message['text'].lower()

    if msg is not None:
        message = msg

    if user_id not in users:
        users[user_id] = UserState(user_id)
        create_state_machine(users[user_id])

    user = users[user_id]
    session = Session()

    if user.state == 'start':
        if message == 'начать':
            categories = session.query(Category).all()
            buttons = [c.name for c in categories]
            send_message(
                user_id,
                'Выберите категорию:',
                create_keyboard(buttons)
            )
            user.view_category()
        else:
            send_message(
                user_id,
                'Отправьте "Начать" для начала работы.'
            )

    elif user.state == 'viewing_category':
        category = session.query(Category).filter_by(
            name=message.capitalize()
        ).first()
        if category:
            user.set_category(category)
            products = session.query(Product).filter_by(
                category_id=category.id
            ).all()
            buttons = [p.name for p in products] + ['Назад']
            send_message(
                user_id,
                f'Товары в категории {category.name}:',
                create_keyboard(buttons)
            )
            user.view_product()
        elif message == 'назад':
            user.back_to_menu()
            handle_event(event, 'начать')
        else:
            send_message(
                user_id,
                'Такой категории нет.'
            )

    elif user.state == 'viewing_product':
        product = session.query(Product).filter_by(
            name=message.capitalize()
        ).first()
        if product:
            send_message(
                user_id,
                f'Название: {product.name}\n'
                f'Описание: {product.description}\n'
                f'Цена: {product.price}\n'
                f'Фото:'
            )
            vk.messages.send(
                user_id=user_id,
                attachment=product.img_url,
                random_id=0
            )
        elif message == 'назад':
            user.back_to_menu()
            handle_event(event, 'начать')
        else:
            send_message(
                user_id,
                'Такого товара нет.'
            )


def main():
    """ Главная функция для запуска бота """
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            handle_event(event)


if __name__ == '__main__':
    main()
