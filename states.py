from transitions import Machine

class UserState:
    states = ['start', 'viewing_category', 'viewing_product']

    def __init__(self, user_id):
        self.user_id = user_id
        self.current_category = None
        self.current_product = None

    def set_category(self, category):
        self.current_category = category

    def set_product(self, product):
        self.current_product = product


def create_state_machine(user):
    """ Создание машины состояний. """
    machine = Machine(model=user, states=UserState.states, initial='start')
    machine.add_transition('view_category', 'start', 'viewing_category')
    machine.add_transition('view_product', 'viewing_category', 'viewing_product')
    machine.add_transition('back_to_menu', '*', 'start')

    return machine
