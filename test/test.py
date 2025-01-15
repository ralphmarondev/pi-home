import tkinter as tk
import threading
import time
import RPi.GPIO as GPIO

# GPIO Pin Setup
LED_PIN = 17  # LED connected to pin 17
BUTTON_PIN = 27  # Push button connected to pin 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)  # Configure LED_PIN as an output
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Configure BUTTON_PIN as an input with pull-up resistor
GPIO.output(LED_PIN, GPIO.LOW)  # Ensure the LED starts off

# GUI Settings
BACKGROUND = '#333333'
FOREGROUND = '#FFFFFF'
FONT = ('Courier New', 16)


class TestFrame:
    def __init__(self, frame: tk.Frame, action):
        self.frame = frame
        self.action = action

    def content(self):
        # Create a subframe for the content
        frame_lights = tk.Frame(master=self.frame, bg=BACKGROUND)
        frame_lights.pack(fill="both", expand=True)

        # Label for lights test
        lights_label = tk.Label(
            master=frame_lights,
            text='Lights Test',
            bg=BACKGROUND,
            fg=FOREGROUND,
            font=FONT
        )
        lights_label.grid(row=0, column=0, pady=10)

        # Button to toggle the LED
        light_button1 = tk.Button(
            master=frame_lights,
            text="Toggle LED (GUI)",
            bg=FOREGROUND,
            fg=BACKGROUND,
            font=FONT,
            command=self.action.toggle_led_gui  # Connect to GUI action
        )
        light_button1.grid(row=1, column=0, pady=5)


class TestAction:
    def __init__(self):
        self.led_state = False  # Track LED state
        self.running = True
        self.thread = threading.Thread(target=self.monitor_push_button)
        self.thread.start()

    def toggle_led_gui(self):
        self._toggle_led()
        print('LED toggled via GUI.')

    def _toggle_led(self):
        # Toggle the LED state
        self.led_state = not self.led_state
        GPIO.output(LED_PIN, GPIO.HIGH if self.led_state else GPIO.LOW)
        print(f'LED is {"ON" if self.led_state else "OFF"}')

    def monitor_push_button(self):
        print('Monitoring push button...')
        while self.running:
            if GPIO.input(BUTTON_PIN) == GPIO.LOW:  # Button pressed (active low)
                print('Push button pressed.')
                self._toggle_led()
                time.sleep(0.5)  # Debounce delay

    def stop(self):
        self.running = False
        self.thread.join()


if __name__ == '__main__':
    try:
        root = tk.Tk()
        root.title("LED Control")
        root.geometry('500x300')

        # Create the action and pass it to the frame
        action = TestAction()
        main_frame = tk.Frame(root)
        main_frame.pack(fill="both", expand=True)

        frame = TestFrame(main_frame, action)
        frame.content()

        def on_close():
            action.stop()  # Stop the push button thread
            GPIO.cleanup()  # Clean up GPIO
            root.destroy()

        root.protocol("WM_DELETE_WINDOW", on_close)
        root.mainloop()
    except Exception as e:
        print(f'Error: {e}')
    finally:
        GPIO.cleanup()  # Ensure GPIO is cleaned up when the app exits