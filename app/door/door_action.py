import threading
import time

from theme import *
from utils.raspberrypi import RaspberryPi

from constants import *


class DoorAction:
    # private:
    def __init__(self):
        self.rpi = RaspberryPi()
        self.state = {
            "door1": False,
            "door2": False,
            "door3": False
        }
        self.door_pins = DOOR_PINS

        self.running = True
        self.thread = threading.Thread(target=self.run_thread)
        self.thread.daemon = True
        print("Starting door monitoring...")

        # Attach servos and initialize door states
        for pin in self.door_pins.values():
            self.rpi.attach_servo(pin)
            self.rpi.set_servo_angle(pin, 0)  # Ensure doors are closed initially

    def start(self):
        print("Starting door thread")
        self.thread.start()

    def stop(self):
        print("Stopping door thread")
        self.running = False
        self.thread.join()

    def run_thread(self):
        print("Door thread started")
        while self.running:
            self.run()
            time.sleep(5)  # Adjust the interval if needed

    def run(self):
        print("Checking door states...")
        for name, pin in self.door_pins.items():
            is_open = self.rpi.is_door_open(pin)
            if self.state[name] != is_open:
                self.state[name] = is_open
                print(f"{name} state changed to {'open' if is_open else 'closed'}")
                self.update_gui(name, is_open)

    def toggle_door(self, name: str):
        if name not in self.door_pins:
            print(f"Invalid door name: {name}")
            return

        current_state = self.state[name]
        pin = self.door_pins[name]

        if current_state:
            self.rpi.set_servo_angle(pin, 0)  # Close the door
            self.state[name] = False
            print(f"Closed {name} via GUI")
        else:
            self.rpi.set_servo_angle(pin, 180)  # Open the door
            self.state[name] = True
            print(f"Opened {name} via GUI")
        self.update_gui(name, self.state[name])

    def update_gui(self, name: str, state: bool):
        door_button = getattr(self, name, None)
        if not door_button:
            print(f"GUI element for {name} not configured.")
            return

        if state:
            door_button.config(bg="orange", fg=FOREGROUND)
        else:
            door_button.config(bg=FOREGROUND, fg=BACKGROUND)

    # public:
    def door1_click(self):
        self.toggle_door("door1")

    def door2_click(self):
        self.toggle_door("door2")

    def door3_click(self):
        self.toggle_door("door3")
