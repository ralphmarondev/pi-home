import threading
import time

from constants import *
from utils.raspberrypi import RaspberryPi


class PhysicalButton:
    def __init__(self):
        print('Physical button is initialized.')
        self.light_button_pins = BUTTON_LED_PINS
        self.led_pins = LED_PINS
        self.running: bool = False
        self.thread = None
        self.rpi = RaspberryPi()

        # Store the states of LEDs
        self.led_states = {button_name: False for button_name in self.light_button_pins}

        # Setup GPIO pins
        for pin in self.light_button_pins.values():
            self.rpi.setup_pin(pin, 'in')
        for pin in self.led_pins.values():
            self.rpi.setup_pin(pin, 'out')

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._monitor_buttons)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

    def _monitor_buttons(self):
        print('Monitoring physical buttons...')
        while self.running:
            for button_name, pin in self.light_button_pins.items():
                if self.rpi.is_light_on(pin):  # Button is pressed
                    print(f'{button_name} is pressed.')
                    self._handle_led_action(button_name)
                    time.sleep(0.5)  # Debounce delay
            time.sleep(0.1)  # Prevent CPU overuse

    def _handle_led_action(self, button_name: str):
        if button_name in self.led_pins:
            led_pin = self.led_pins[button_name]
            self._toggle_led(led_pin, button_name)

    def _toggle_led(self, led_pin: int, button_name: str):
        # Toggle the LED state
        self.led_states[button_name] = not self.led_states[button_name]
        if self.led_states[button_name]:
            self.rpi.open_light(led_pin)
            print(f'LED on {led_pin} turned ON.')
        else:
            self.rpi.close_light(led_pin)
            print(f'LED on {led_pin} turned OFF.')
