from machine import Pin
import time

LED = Pin(2,Pin.OUT)
BUT = Pin(0,Pin.IN)
while True:
    but_status = BUT.value()
    if(but_status == False):
        LED.value(1)
    else:
        LED.value(0)