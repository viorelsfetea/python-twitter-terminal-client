from controller import Controller


class TwitterClientInterface(object):

    controller = Controller()

    def __init__(self):
        self.controller.init_view()
        self.controller.set_available_commands()
        self.controller.init_command_listener()

if __name__ == '__main__':
    TwitterClientInterface()
