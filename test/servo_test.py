import time
import tkinter as tk

import RPi.GPIO as GPIO


class ServoTest(tk.Tk):
    def __init__(self):
        super().__init__()
        self.action = ServoTestAction()

        self.title('Servo Test')
        self.configure(bg='#333333')
        self.geometry('500x300')
        self.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.content()

    def on_closing(self):
        self.destroy()

    def content(self):
        frame = tk.Frame(
            master=self,
            bg='#333333'
        )
        title_label = tk.Label(
            master=frame,
            text='Servo Test',
            bg='#333333',
            fg='#ffffff',
            font=('monospace', 16)
        )
        button = tk.Button(
            master=frame,
            text='CLICK ME',
            font=('monospace', 16),
            command=self.action.on_click
        )

        title_label.grid(row=0, column=0, pady=5)
        button.grid(row=1, column=0, pady=5)

        frame.pack()

        # REFERENCE
        self.action.button = button


class ServoTestAction:
    def __init__(self):
        self.state = {
            "button": False
        }
        self.servo_pin = 17  # pin for servo
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.servo_pin, GPIO.OUT)
        self.servo = GPIO.PWM(self.servo_pin, 50)  # 50Hz for servo
        self.servo.start(0)  # initialize servo position

    def __toggle(self, name: str):
        button = getattr(self, 'button', None)
        if not button:
            print('Some error')
            return

        if self.state[name]:
            button.config(bg='#ffffff')
            self.state[name] = False
            self.door_close()
        else:
            button.config(bg='orange')
            self.state[name] = True
            self.door_open()

    def on_click(self):
        self.__toggle('button')

    def door_open(self):
        # TODO: Open door [rotate servo]
        print('Opening door...')
        # 7.5 = 2.5 + (90degrees/18.0) 0deg = 2.5%, 18.0 = 180 deg = 12.5%
        self.servo.ChangeDutyCycle(7.5)  # 90 degrees
        time.sleep(1)  # delay for servo to reach to position

    def door_close(self):
        # TODO: Close door [rotate the servo back to its original angle]
        print('Closing door...')
        self.servo.ChangeDutyCycle(2.5)  # 0 degrees
        time.sleep(1)

    def cleanup(self):
        self.servo.stop()
        GPIO.cleanup()
        print('GPIO cleaned up')


# Servo config
# Red [VCC] 5v or 3.3v on rpi
# Brown/Black [GND] ground pin on rpi
# Yellow/Orange [Signal] -> GPIO17
if __name__ == '__main__':
    app = ServoTest()

    app.mainloop()
