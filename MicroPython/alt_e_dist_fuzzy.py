from machine import Pin
from machine import Timer
from hcsr04 import HCSR04
import machine
import time

LED = machine.Pin(2, machine.Pin.OUT)
sensor_distancia = HCSR04(trigger_pin=21, echo_pin=22, echo_timeout_us=1000000)
#sensor_altura = HCSR04(trigger_pin=25, echo_pin=26, echo_timeout_us=1000000)

led_state = 0  # 0 for off, 1 for on

def fuzzy_logic(altura, distancia):
    if (40 < altura <= 400) or (distancia < 10):
        return 125  # Pisca muito rapido
    elif (20 < altura <= 40) or (distancia < 20):
        return 250  # Piscando rapido
    elif (10 <= altura <= 20) or (distancia < 40):
        return 500  # Piscando devagar
    elif (altura < 10 and distancia > 40) or (altura > 400 and distancia > 40):
        return 0  # nao pisca
    else:
        return 0  # Desligado

def timer0_callback(timer):
    global led_state
    distancia = sensor_distancia.distance_cm()
    #altura = sensor_altura.distance_cm()
    #distancia = 42
    altura = 0;
    print('Distancia: {}cm'.format(round(distancia, 2)))
    print('Altura: {}cm'.format(round(altura, 2)))
    led_pwm = fuzzy_logic(altura,distancia)
    print('Velocidade: {}ms'.format(round(led_pwm, 2)))
    if led_pwm != 0:
        if led_state == 0:
            LED.value(1)
            led_state = 1
        else:
            LED.value(0)
            led_state = 0
        timer0.init(period=led_pwm, mode=Timer.PERIODIC, callback=timer0_callback)  # Double the speed

timer0 = Timer(0)
timer0.init(period=500, mode=Timer.PERIODIC, callback=timer0_callback)