import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
inPin = 4
LEDPin = 17
GPIO.setup(inPin, GPIO.IN)
GPIO.setup(LEDPin, GPIO.OUT)
delayTime = 0.25

try:
    while True:
        readValue = GPIO.input(inPin)
        print(readValue)
        if readValue == 0:
            GPIO.output(LEDPin, True)
        else:
            GPIO.output(LEDPin, False)
        sleep(delayTime)
except KeyboardInterrupt:
    GPIO.cleanup()
