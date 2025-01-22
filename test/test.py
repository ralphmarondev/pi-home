import time
import tkinter as tk

import RPi.GPIO as GPIO

SERVO_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)

is_open: bool = False


def set_servo_angle(angle):
    duty = 2 + (angle / 18)
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)


def open_door():
    print('opening door')
    set_servo_angle(180)


def close_door():
    print('closing door')
    set_servo_angle(0)


def toggle_door():
    global is_open
    if is_open:
        close_door()
    else:
        open_door()

    is_open = not is_open
    print(f'Door state, is_open: {is_open}')


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Testing Servo")
    root.geometry("500x300")

    button = tk.Button(
        master=root,
        text="Open Servo",
        command=toggle_door
    )
    button.grid(row=0, column=1, pady=5, padx=5)

    root.mainloop()
