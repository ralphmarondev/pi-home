import RPi.GPIO as GPIO

class RaspberryPi:
    def __init__(self):
        print('Initializing Raspberry Pi GPIO...')
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.servos = {}

    def setup_pin(self, pin: int, mode: str):
        print(f'Setting up pin: {pin} => {mode}')
        if mode == "in":
            GPIO.setup(pin, GPIO.IN)
        elif mode == "out":
            GPIO.setup(pin, GPIO.OUT)

    def is_light_on(self, pin: int):
        return GPIO.input(pin) == GPIO.HIGH

    def open_light(self, pin: int):
        GPIO.output(pin, GPIO.HIGH)
        print(f'opening light {pin}')

    def close_light(self, pin: int):
        GPIO.output(pin, GPIO.LOW)
        print(f'closing light {pin}')

    # doors
    def attach_servo(self, pin: int):
        if pin not in self.servos:
            self.servos[pin] = 0  # default angle 0
            print(f'Attaching servo to pin: {pin}')
            GPIO.setup(pin, GPIO.OUT)
            self.servos[pin] = GPIO.PWM(pin, 50)
            self.servos[pin].start(0)
        else:
            print(f'Servo already attached to pin: {pin}')

    def set_servo_angle(self, pin: int, angle: int):
        if pin not in self.servos:
            print(f'No servo attached to pin {pin}. Attaching one now.')
            self.attach_servo(pin)

        if not (0 <= angle <= 180):
            print(f'Invalid angle: {angle}. Must be between 0 and 180.')
            return

        duty_cycle = self.__angle_to_duty_cycle(angle)
        print(f'Setting servo on pin {pin} to angle {angle} {duty_cycle: {duty_cycle}}')
        self.servos[pin] = angle
        self.servos[pin].ChangeDutyCycle(duty_cycle)
        time.sleep(0.3)
        self.servos[pin].ChangeDutyCycle(0)

    def __angle_to_duty_cycle(self, angle: int):
        return (0.05 * angle) + 2.5

    def detach_servo(self, pin: int):
        if pin in self.servos:
            print(f'Detaching servo from pin: {pin}')
            self.servos[pin].stop()
            del self.servos[pin]
        else:
            print(f'No servo attached to pin: {pin}')

    def is_door_open(self, pin: int):
        if pin in self.servos:
            return self.servos[pin] == 90
        print(f'No servo attached to pin {pin}')
        return False

    def cleanup(self):
        print('Cleaning up GPIO...')
        GPIO.cleanup()
