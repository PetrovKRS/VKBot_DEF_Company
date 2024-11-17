from bot import send_message

def test_send_message(mocker):
    """ Проверяет отправку сообщений через API. """
    vk_mock = mocker.patch("bot.vk.messages.send")
    send_message(
        user_id=1,
        message='Тест',
        keyboard=None
    )
    vk_mock.assert_called_once_with(
        user_id=1,
        message='Тест',
        random_id=0,
        keyboard=None
    )
