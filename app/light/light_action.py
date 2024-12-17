import threading
import time

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
        self.count = 0

        self.running = True
        self.thread = threading.Thread(target=self.run_thread)
        self.thread.daemon = True
        print('starting light initialized')

    def run_thread(self):
        print('light thread started')
        while self.running:
            self.run()
            time.sleep(5)

    def start(self):
        print('starting light thread')
        self.thread.start()

    def stop(self):
        print('stopping light thread')
        self.running = False
        self.thread.join()

    # TODO: Update this to implement the actual logic.
    # TODO: What matters now is thread is running!
    def run(self):
        print('light thread triggered')
        print(f'Count: {self.count}')
        name = 'light1'
        light = getattr(self, name, None)
        if not light:
            print(f'{light} is not configured.')
            return

        if self.count % 2 == 0:
            self.state[name] = False
            light.config(
                bg=FOREGROUND,
                fg='#333333'
            )
            self.__close_light(name)
        else:
            self.state[name] = True
            light.config(
                bg='#FF9800',
                fg='#ffffff'
            )
            self.__open_light(name)
        self.count += 1

    def __toggle(self, name: str):
        light = getattr(self, name, None)
        if not light:
            print('Some error')
            return

        if self.state[name]:
            light.config(
                bg=FOREGROUND,
                fg='#333333'
            )
            self.state[name] = False
            self.__close_light(name)
        else:
            light.config(
                bg='#FF9800',
                fg='#ffffff'
            )
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
