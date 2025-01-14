import threading
import time

from app.constants import *
from app.utils.raspberrypi import RaspberryPi


class PhysicalButton:
    def __init__(self):
        self.light_button_pins = BUTTON_LED_PINS
        self.led_pins = LED_PINS
        self.door_button_pins = BUTTON_DOOR_PINS
        self.door_pins = DOOR_PINS

        self.running: bool = False
        self.thread = None
        self.rpi = RaspberryPi()

        # Setup GPIO pins
        for pin in self.light_button_pins.values():
            self.rpi.setup_pin(pin, 'in')
        for pin in self.led_pins.values():
            self.rpi.setup_pin(pin, 'out')
        for pin in self.door_button_pins.value():
            self.rpi.setup_pin(pin, 'in')
        for pin in self.door_pins.values():
            self.rpi.attach_servo(pin)

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
            for button_name, pin in self.light_button_pins.items():
                if self.rpi.is_light_on(pin):
                    print(f'{button_name} is pressed.')
                    self._handle_led_action(button_name)
                    time.sleep(0.5)  # Debounce to avoid multiple triggers

            # for doors
            for button_name, pin in self.door_button_pins.items():
                if self.rpi.is_light_on(pin):
                    print(f'{button_name} button is pressed.')
                    self._handle_door_action(button_name)
                    time.sleep(0.5)

    def _handle_led_action(self, button_name: str):
        if button_name in self.led_pins:
            led_pin = self.led_pins[button_name]
            self._toggle_led(led_pin)

    def _toggle_led(self, led_pin: int):
        if self.rpi.is_light_on(led_pin):
            self.rpi.close_light(led_pin)
        else:
            self.rpi.open_light(led_pin)

    def _handle_door_action(self, button_name: str):
        if button_name in self.door_pins:
            door_pin = self.door_pins[button_name]
            self._toggle_door(door_pin)

    def _toggle_door(self, door_pin: int):
        if self.rpi.is_door_open(door_pin):
            self.rpi.set_servo_angle(door_pin, 0)
            print(f'Door on pin {door_pin} closed.')
        else:
            self.rpi.set_servo_angle(door_pin, 90)
            print(f'Door on pin {door_pin} opened.')
