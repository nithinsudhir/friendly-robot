from model.user import User

class Hospital(User):
    def __init__(self, system):
        self.system = system
        self.user_type = 'Hospital'

    def print_instructions(self):
        print('This system accepts the following commands:')
        print('request - request a specific blood type')
        print('help - print all available commands\n\n')