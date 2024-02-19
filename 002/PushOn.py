from machine import Pin
import time

LED = Pin(16, Pin.OUT)
BUTTON = Pin(15, Pin.IN, Pin.PULL_DOWN)
LED.value(0)

while True:
    if BUTTON.value():
        LED.value(1)
    else:
        LED.value(0)