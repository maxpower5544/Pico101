from machine import Pin
import time

LED = Pin(16, Pin.OUT)
BUTTON = Pin(15, Pin.IN, Pin.PULL_DOWN)
VAL = 0

while True:
    if BUTTON.value():
        VAL += 1
        time.sleep(0.2)
    elif VAL >= 2:
        VAL = 0
        time.sleep(0.2)
    LED.value(VAL)