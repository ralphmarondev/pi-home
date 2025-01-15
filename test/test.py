import tkinter as tk
import RPi.GPIO as GPIO

BACKGROUND = '#333333'
FOREGROUND = '#FFFFFF'
FONT = ('Courier New', 16)

# GPIO Setup
LED_PIN = 17  # Pin where the LED is connected
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)  # Configure LED_PIN as an output
GPIO.output(LED_PIN, GPIO.LOW)  # Ensure the LED starts off


class TestFrame:
    def __init__(self, frame: tk.Frame):
        self.frame = frame
        self.action = TestAction()

    def content(self):
        # Create a subframe for the content
        frame_lights = tk.Frame(master=self.frame, bg=BACKGROUND)
        frame_lights.pack(fill="both", expand=True)  # Ensure it fills the parent frame

        # Label for the lights test
        lights_label = tk.Label(
            master=frame_lights,
            text='Lights Test',
            bg=BACKGROUND,
            fg=FOREGROUND,
            font=FONT
        )
        lights_label.grid(row=0, column=0, pady=10)

        # Button to open the light
        light_button1 = tk.Button(
            master=frame_lights,
            text="Toggle LED",
            bg=FOREGROUND,
            fg=BACKGROUND,
            font=FONT,
            command=self.action.toggle_led  # Connect to GPIO logic
        )
        light_button1.grid(row=1, column=0, pady=5)

        # Store button reference in the action object (optional, if needed later)
        self.action.light_button = light_button1


class TestAction:
    def __init__(self):
        self.led_state = False  # Track LED state

    def toggle_led(self):
        self.led_state = not self.led_state  # Toggle the state
        if self.led_state:
            GPIO.output(LED_PIN, GPIO.HIGH)
            print('LED is ON')
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            print('LED is OFF')


if __name__ == '__main__':
    try:
        root = tk.Tk()

        # Configure the root window
        root.title("Light Test")
        root.geometry('500x300')

        # Create a TestFrame with the root as the parent
        main_frame = tk.Frame(root)
        main_frame.pack(fill="both", expand=True)

        frame = TestFrame(main_frame)
        frame.content()

        root.mainloop()
    finally:
        GPIO.cleanup()  # Ensure GPIO is cleaned up when the app closes
