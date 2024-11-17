import bot  # Импортируем модуль, чтобы мокнуть его атрибут
from bot import send_message  # Импортируем тестируемую функцию
from vk_api import VkApi  # Импортируем класс для спецификации


def test_send_message(mocker):
    """ Проверяет отправку сообщений через API. """

    # Создаем mock для объекта VkApi
    vk_method_mock = mocker.MagicMock()
    messages_mock = mocker.MagicMock()
    vk_method_mock.messages = messages_mock

    # Мокаем объект vk в модуле bot
    mocker.patch.object(bot, "vk", vk_method_mock)

    # Вызываем тестируемую функцию
    send_message(
        user_id=123,
        message="Привет",
        keyboard="{}"
    )

    # Проверяем вызов метода send с нужными аргументами
    messages_mock.send.assert_called_once_with(
        user_id=123,
        random_id=mocker.ANY,
        message="Привет",
        keyboard="{}"
    )
