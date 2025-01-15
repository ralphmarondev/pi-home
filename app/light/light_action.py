import threading
import time

from theme import *
from utils.raspberrypi import RaspberryPi

from constants import LED_PINS


class LightAction:
    # private:
    def __init__(self):
        self.rpi = RaspberryPi()
        self.state = {
            "light1": False,
            "light2": False,
            "light3": False
        }
        self.light_pins = LED_PINS

        self.running = True
        self.thread = threading.Thread(target=self.run_thread)
        self.thread.daemon = True
        print('starting light initialized')

        # setup gpio pins as output
        for pin in self.light_pins.values():
            self.rpi.setup_pin(pin=pin, mode='out')

    def start(self):
        print('starting light thread')
        self.thread.start()

    def stop(self):
        print('stopping light thread')
        self.running = False
        self.thread.join()

    def run_thread(self):
        print('light thread started')
        while self.running:
            self.run()
            time.sleep(5)

    def run(self):
        print('Checking light states')
        for name, pin in self.light_pins.items():
            state = self.rpi.is_light_on(pin)
            if self.state[name] != state:
                self.state[name] = state
                print(f'{name} state changed to ', end='')
                if state:
                    print('on')
                else:
                    print('off')
                self.update_gui(name, state)

    def toggle_light(self, name: str):
        if name not in self.light_pins:
            print(f'Invalid light name: {name}')
            return

        current_state = self.state[name]
        pin = self.light_pins[name]

        if current_state:
            self.rpi.close_light(pin)
            self.state[name] = False
            print(f'Turned off {name} via GUI')
        else:
            self.rpi.open_light(pin)
            self.state[name] = True
            print(f'Turned on {name} via GUI')
        self.update_gui(name, self.state[name])

    def update_gui(self, name: str, state: bool):
        light_button = getattr(self, name, None)
        if not light_button:
            print(f'GUI element for {name} not configured.')
            return

        if state:
            light_button.config(bg='#FF9800', fg=FOREGROUND)
        else:
            light_button.config(bg=FOREGROUND, fg=BACKGROUND)

    # public:
    def light1_click(self):
        self.toggle_light('light1')

    def light2_click(self):
        self.toggle_light('light2')

    def light3_click(self):
        self.toggle_light('light3')
