class RaspberryPi:
    def setup_pin(self, pin: int, mode: str):
        print(f'Setting up pin: {pin} => {mode}')
        # if mode == "in":
        #     GPIO.setup(pin, GPIO.IN)
        # elif mode == "out":
        #     GPIO.setup(pin, GPIO.OUT)

    def is_light_on(self, pin: int):
        # return GPIO.input(pin) == GPIO.HIGH
        return False

    def open_light(self, pin: int):
        # GPIO.output(pin, GPIO.HIGH)
        print(f'opening light {pin}')

    def close_light(self, pin: int):
        # GPIO.output(pin, GPIO.LOW)
        print(f'closing light {pin}')
