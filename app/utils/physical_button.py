import threading
import time

from constants import *
from utils.raspberrypi import RaspberryPi


class PhysicalButton:
    def __init__(self, debug=False):
        print('Initializing Physical Button...')
        self.debug = debug
        self.light_button_pins = BUTTON_LED_PINS
        self.led_pins = LED_PINS
        self.running: bool = False
        self.thread = None
        self.rpi = RaspberryPi()

        # Track button states
        self.button_states = {button_name: False for button_name in self.light_button_pins}
        self.led_states = {button_name: False for button_name in self.light_button_pins}

        # Setup GPIO pins
        for pin in self.light_button_pins.values():
            self.rpi.setup_pin(pin, 'in')
        for pin in self.led_pins.values():
            self.rpi.setup_pin(pin, 'out')

    def start(self):
        print("Starting button monitoring...")
        self.running = True
        self.thread = threading.Thread(target=self._monitor_buttons, daemon=True)
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
                current_state = self.rpi.is_light_on(pin)
                previous_state = self.button_states[button_name]

                # Detect button press transition (rising edge)
                if current_state and not previous_state:
                    self._debug_log(f"{button_name} pressed.")
                    self._toggle_led(button_name)

                # Update button state
                self.button_states[button_name] = current_state

            time.sleep(0.1)  # Reduce CPU usage and debounce

    def _toggle_led(self, button_name: str):
        if button_name in self.led_pins:
            led_pin = self.led_pins[button_name]

            # Toggle the LED state
            self.led_states[button_name] = not self.led_states[button_name]
            if self.led_states[button_name]:
                self.rpi.open_light(led_pin)
                print(f"{button_name} LED turned ON (pin {led_pin}).")
            else:
                self.rpi.close_light(led_pin)
                print(f"{button_name} LED turned OFF (pin {led_pin}).")

    def _debug_log(self, message: str):
        if self.debug:
            print(f"[DEBUG] {message}")
