from app.theme import *


class LightAction:
    # private:
    def __init__(self):
        self.state = {
            "light1": False,
            "light2": False,
            "light3": False
        }
        self.light1_pin = 0
        self.light2_pin = 2
        self.light3_pin = 4

    def __toggle(self, name: str):
        light = getattr(self, name, None)
        if not light:
            print('Some error')
            return

        if self.state[name]:
            light.config(bg=FOREGROUND)
            self.state[name] = False
            self.__close_light(name)
        else:
            light.config(bg='orange')
            self.state[name] = True
            self.__open_light(name)

    def __open_light(self, name: str):
        print(f'Opening light: {name}')

    def __close_light(self, name: str):
        print(f'Closing light: {name}')

    # public:
    def light1_click(self):
        self.__toggle('light1')

    def light2_click(self):
        self.__toggle('light2')

    def light3_click(self):
        self.__toggle('light3')
