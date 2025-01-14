"""
NOTES:
    DOOR SERVO FORMULA:
        7.5 = 2.5 + (90degrees/18.0) 0deg = 2.5%, 18.0 = 180 deg = 12.5%

    SERVO CONFIGURATION:
        Red [VCC] 5v or 3.3v on rpi
        Brown/Black [GND] ground pin on rpi
        Yellow/Orange [Signal] -> GPIO17
"""

# pins for led
BUTTON_LED_PINS = {
    'button1': 17,
    'button2': 27,
    'button3': 22
}

LED_PINS = {
    'button1': 5,
    'button2': 6,
    'button3': 13
}

# pins for servo
BUTTON_DOOR_PINS = {
    'button1': 10,
    'button2': 11,
    'button3': 12
}

DOOR_PINS = {
    'button1': 0,
    'button2': 2,
    'button3': 4
}