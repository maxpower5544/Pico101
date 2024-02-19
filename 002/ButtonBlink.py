from machine import Pin
import time

LED = Pin(16, Pin.OUT)
BUTTON = Pin(15, Pin.IN, Pin.PULL_DOWN)

while True:
    while BUTTON.value()==0:
        pass
    h=time.ticks_ms()
    time.sleep_ms(1)
    while BUTTON.value()==1:
        pass
    h=time.ticks_diff(time.ticks_ms(),h)
    if h<2000:
        LED.on()
        time.sleep(1)
        LED.off()
    else:
        for i in range(10):
            LED.on()
            time.sleep_ms(100)
            LED.off()
            time.sleep_ms(100)