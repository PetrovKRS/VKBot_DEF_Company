from bot import handle_event


def test_handle_event_start(mocker):
    """ Проверяет обработку команды 'Начать'. """
    mock_event = mocker.Mock()
    mock_event.message = {'from_id': 1, 'text': 'Начать'}

    send_mock = mocker.patch("bot.send_message")
    session_mock = mocker.patch("bot.Session", return_value=mocker.Mock())
    session_mock.return_value.query.return_value.all.return_value = []

    handle_event(mock_event)

    send_mock.assert_called_once_with(
        1,
        "Выберите категорию:",
        '{"one_time": false, "buttons": []}'
    )