from app.theme import *


class DoorAction:
    # private:
    def __init__(self):
        self.state = {
            "door1": False,
            "door2": False,
            "door3": False
        }
        self.door1_pin = 0
        self.door2_pin = 2
        self.door3_pin = 4

    def __toggle(self, name: str):
        door = getattr(self, name, None)
        if not door:
            print('Some error')
            return

        if self.state[name]:
            door.config(bg=FOREGROUND)
            self.state[name] = False
            self.__close_door(name)
        else:
            door.config(bg='orange')
            self.state[name] = True
            self.__open_door(name)

    def __open_door(self, name: str):
        print(f'Opening door: {name}')

    def __close_door(self, name: str):
        print(f'Closing door: {name}')

    # public:
    def door1_click(self):
        self.__toggle('door1')

    def door2_click(self):
        self.__toggle('door2')

    def door3_click(self):
        self.__toggle('door3')
