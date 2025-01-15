import threading
import time
from utils.raspberrypi import RaspberryPi

# Constants for GPIO pins (defined in a separate constants file)
# Example:
# BUTTON_LED_PINS = {"button1": 27, "button2": 22}
# LED_PINS = {"button1": 17, "button2": 23}
from constants import BUTTON_LED_PINS, LED_PINS


class ButtonLEDController:
    def __init__(self):
        self.rpi = RaspberryPi()
        self.running = False
        self.led_states = {key: False for key in LED_PINS}  # Track LED states
        self.thread = None

        # Store the mapping of buttons to LEDs
        self.light_button_pins = BUTTON_LED_PINS
        self.led_pins = LED_PINS

        # Setup GPIO pins
        for pin in self.light_button_pins.values():
            self.rpi.setup_pin(pin, 'in')  # Buttons as input
        for pin in self.led_pins.values():
            self.rpi.setup_pin(pin, 'out')  # LEDs as output

    def start(self):
        """Start monitoring the buttons."""
        self.running = True
        self.thread = threading.Thread(target=self._monitor_buttons, daemon=True)
        self.thread.start()
        print("Button-LED controller started.")

    def stop(self):
        """Stop monitoring the buttons."""
        self.running = False
        if self.thread:
            self.thread.join()
        print("Button-LED controller stopped.")

    def _monitor_buttons(self):
        """Thread function to monitor the buttons and toggle LEDs."""
        print("Monitoring buttons...")
        previous_states = {key: False for key in self.light_button_pins}

        while self.running:
            for button_name, button_pin in self.light_button_pins.items():
                # Read the current state of the button
                current_state = self.rpi.is_light_on(button_pin)

                # Detect rising edge (button press)
                if current_state and not previous_states[button_name]:
                    self._toggle_led(button_name)

                # Update the previous state
                previous_states[button_name] = current_state

            time.sleep(0.05)  # Polling interval to reduce CPU usage

    def _toggle_led(self, button_name: str):
        """Toggle the LED state for the given button name."""
        if button_name in self.led_pins:
            led_pin = self.led_pins[button_name]
            # Toggle the LED state
            self.led_states[button_name] = not self.led_states[button_name]
            if self.led_states[button_name]:
                self.rpi.open_light(led_pin)
                print(f"LED for {button_name} turned ON.")
            else:
                self.rpi.close_light(led_pin)
                print(f"LED for {button_name} turned OFF.")


if __name__ == "__main__":
    # Create the controller instance
    controller = ButtonLEDController()

    try:
        # Start the controller
        controller.start()

        # Keep the main thread alive
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        # Stop the controller on Ctrl+C
        controller.stop()
        print("Exiting program.")
