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
    'light1': 5,
    'light2': 6,
    'light3': 13
}

# pins for servo
BUTTON_DOOR_PINS = {
    'button1': 12,
    'button2': 16,
    'button3': 20
}

DOOR_PINS = {
    'door1': 23,
    'door2': 24,
    'door3': 25
}