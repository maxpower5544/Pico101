from machine import Pin
import time

LED = Pin("LED", Pin.OUT)
LED.value(0)

while True:
    LED.value(1)
    time.sleep(0.5)
    LED.value(0)
    time.sleep(0.5)