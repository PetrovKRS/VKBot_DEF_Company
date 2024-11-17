from states import UserState, create_state_machine

def test_state_machine():
    """ Проверяет работу машины состояний. """
    user = UserState(user_id=1)
    machine = create_state_machine(user)

    # Начальное состояние
    assert user.state == "start"

    # Переход в состояние просмотра категории
    user.view_category()
    assert user.state == "viewing_category"

    # Переход в состояние просмотра товара
    user.view_product()
    assert user.state == "viewing_product"

    # Возврат в меню
    user.back_to_menu()
    assert user.state == "start"
