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

        # Store the states of LEDs and buttons
        self.led_states = {button_name: False for button_name in self.light_button_pins}
        self.button_states = {button_name: False for button_name in self.light_button_pins}

        # Setup GPIO pins
        for pin in self.light_button_pins.values():
            print(f"Setting up button pin: {pin}")
            self.rpi.setup_pin(pin, 'in')

        for pin in self.led_pins.values():
            print(f"Setting up LED pin: {pin}")
            self.rpi.setup_pin(pin, 'out')

    def start(self):
        print("Starting button monitoring...")
        self.running = True
        self.thread = threading.Thread(target=self._monitor_buttons)
        self.thread.start()

    def stop(self):
        print("Stopping button monitoring...")
        self.running = False
        if self.thread:
            self.thread.join()

    def _monitor_buttons(self):
        print('Monitoring physical buttons...')
        while self.running:
            for button_name, pin in self.light_button_pins.items():
                current_state = not self.rpi.is_light_on(pin)  # Adjust based on button logic
                previous_state = self.button_states[button_name]

                print(f"[DEBUG] {button_name} - Current State: {current_state}, Previous State: {previous_state}")

                # Detect button press (transition from not pressed to pressed)
                if current_state and not previous_state:
                    print(f"{button_name} is pressed. Toggling LED.")
                    self._handle_led_action(button_name)

                # Update button state
                self.button_states[button_name] = current_state

            time.sleep(0.1)  # Polling interval to reduce CPU usage

    def _handle_led_action(self, button_name: str):
        if button_name in self.led_pins:
            led_pin = self.led_pins[button_name]
            self._toggle_led(led_pin, button_name)

    def _toggle_led(self, led_pin: int, button_name: str):
        # Toggle the LED state
        self.led_states[button_name] = not self.led_states[button_name]
        if self.led_states[button_name]:
            self.rpi.open_light(led_pin)
            print(f"LED on pin {led_pin} turned ON.")
        else:
            self.rpi.close_light(led_pin)
            print(f"LED on pin {led_pin} turned OFF.")
