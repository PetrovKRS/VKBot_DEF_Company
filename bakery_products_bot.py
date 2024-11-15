import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import os
import dotenv
import sqlite3
import json

dotenv.load_dotenv()

VK_TOKEN = os.getenv('VK_TOKEN')
vk_session = vk_api.VkApi(token=VK_TOKEN)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

conn = sqlite3.connect(os.getenv('DB_NAME'), check_same_thread=False)
cursor = conn.cursor()


def get_categories():
    """ Получаем список категорий. """
    cursor.execute(
        '''
            SELECT id, name 
            FROM categories;
        '''
    )
    return cursor.fetchall()


def get_products_by_category(category_id):
    """ Получаем список продуктов по категории. """
    cursor.execute(
    '''
            SELECT id, name, description, img_url, price
            FROM products 
            WHERE category_id = ?;
        ''',(category_id,)
    )
    return cursor.fetchall()


def send_message(user_id, message, keyboard=None):
    """ Отправка сообщения пользователю. """
    vk.messages.send(
        user_id=user_id,
        message=message,
        random_id=0,
        keyboard=keyboard
    )


def create_menu(buttons):
    """ Менюшка с кнопками. """
    menu = {
        'one_time': True,
        'buttons':
        [
            [
                {
                    'action': {
                        'type': 'text',
                        'label': button
                    },
                    'color': 'primary'
                }
            ] for button in buttons
        ]
    }
    return json.dumps(menu, ensure_ascii=False)


def handle_message(event):
    """ Обработка сообщений пользователей. """
    if event.text.lower() == 'каталог':
        categories = get_categories()
        category_names = [category[1] for category in categories]
        menu = create_menu(category_names + ['Назад'])
        send_message(event.user_id, 'Выберите категорию:', menu)

    elif event.text in [category[1] for category in get_categories()]:
        category_id = [category[0] for category in get_categories() if category[1] == event.text][0]
        products = get_products_by_category(category_id)

        for product in products:
            product_info = (
                f'* Название: {product[1]} \n'
                f'* Описание: {product[2]} \n'
                f'* Цена: {product[4]} \n'
            )
            send_message(event.user_id, product_info)

            # Если в БД есть ссылка на изображение
            if product[3]:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=0,
                    attachment=product[3]
                )

        send_message(
            event.user_id,
            'Назад в каталог',
            create_menu(['Каталог'])
        )

    elif event.text.lower() == 'назад':
        send_message(
            event.user_id,
            'Возврат в главное меню',
            create_menu(['Каталог'])
        )
    else:
        send_message(
            event.user_id,
            'Неизвестная команда, используйте меню.'
        )


def main():
    """ Основная логика работы бота. """
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            handle_message(event)


if __name__ == '__main__':
    main()
