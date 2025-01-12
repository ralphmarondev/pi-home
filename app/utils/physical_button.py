import threading
import time

from app.constants import BUTTON_LED_PINS, LED_PINS
from app.utils.raspberrypi import RaspberryPi


class PhysicalButton:
    def __init__(self):
        self.button_pins = BUTTON_LED_PINS
        self.led_pins = LED_PINS
        self.running: bool = False
        self.thread = None
        self.rpi = RaspberryPi()

        # Setup GPIO pins
        for pin in button_pins.values():
            self.rpi.setup_pin(pin, 'in')
        for pin in led_pins.values():
            self.rpi.setup_pin(pin, 'out')

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._monitor_buttons)

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

    def _monitor_buttons(self):
        print('Monitoring physical buttons...')
        while self.running:
            for button_name, pin in self.button_pins.items():
                if self.rpi.is_light_on(pin):
                    print(f'{button_name} is pressed.')
                    self._handle_button_action(button_name)
                    time.sleep(0.5)  # Debounce to avoid multiple triggers

    def _handle_button_action(self, button_name: str):
        if button_name in self.led_pins:
            led_pin = self.led_pins[button_name]
            self._toggle_led(led_pin)

    def _toggle_led(self, led_pin: int):
        if self.rpi.is_light_on(led_pin):
            self.rpi.close_light(led_pin)
        else:
            self.rpi.open_light(led_pin)
