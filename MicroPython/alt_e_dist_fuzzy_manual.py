from machine import Pin
from machine import Timer
from hcsr04 import HCSR04
import machine
import time

LED = machine.Pin(2, machine.Pin.OUT)
sensor_distancia = HCSR04(trigger_pin=21, echo_pin=22, echo_timeout_us=1000000)
#sensor_altura = HCSR04(trigger_pin=25, echo_pin=26, echo_timeout_us=1000000)

pisca_muito_rapido = 125 #125ms
pisca_rapido = 250  #250ms
pisca_devagar = 500 #500ms

led_state = 0  # 0 for off, 1 for on

#funcoes de pertinencia para o sensor de distancia
def distancia_baixa(x):
    if x < 10:
        return 1
    return 0
def distancia_media(x):
    if x > 10 and x < 20:
        return 1
    return 0
def distancia_alta(x):
    if x > 20 and x < 40:
        return 1
    return 0
def distancia_muito_alta(x):
    if x > 40:
        return 1
    return 0

#funções de pertinencia para altura
def altura_baixa(x):
    if x < 10:
        return 1
    return 0
def altura_media(x):
    if x > 10 and x < 20:
        return 1
    return 0
def altura_alta(x):
    if x > 20 and x < 40:
        return 1
    return 0
def altura_muito_alta(x):
    if x > 40:
        return 1
    return 0

# Inferencia Fuzzy
# Calculo do grau de pertinencia
def fuzzy_inference(altura,distancia,regra):
    if regra == "R1":
        #Altura muito alta OU distancia baixa
        #Pisca muito rápido
        return(max(altura_muito_alta(altura),distancia_baixa(distancia)))
    if regra == "R2":
        #Altura alta OU distancia media
        #Pisca rápido
        return(max(altura_alta(altura),distancia_media(distancia)))
    if regra == "R3":
        #Altura média OU distancia alta
        #Pisca devagar
        return(max(altura_media(altura),distancia_alta(distancia)))
    if regra == "R4":
        #Altura baixa ou distancia muito alta
        #nao pisca
        return(max(altura_baixa(altura),distancia_muito_alta(distancia)))

regras = [
    ("R1", fuzzy_inference(altura,distancia,"R1")),
    ("R2", fuzzy_inference(altura,distancia,"R2")),
    ("R3", fuzzy_inference(altura,distancia,"R3"))
]

# Função para controlar o LED com base na lógica fuzzy
def controlar_led(timer):
    #altura = sensor_altura.distance_cm() 
    altura = 0
    distancia = sensor_distancia.distance_cm() 
    # Calcula o grau de pertinência com base na lógica fuzzy
    defuzzified_value = 0
    total_weight = 0
    for regra, valor in regras:
        defuzzified_value += valor * fuzzy_inference(altura, distancia, regra)
        total_weight += valor

    if total_weight > 0:
        defuzzified_value /= total_weight
        


    # Determine o intervalo de piscagem com base no resultado fuzzy
    if defuzzified_value > 0.7:  # Por exemplo, um valor de corte para "piscar muito rápido"
        intervalo = intervalo_muito_rapido
    elif defuzzified_value > 0.3:  # Por exemplo, um valor de corte para "piscar rápido"
        intervalo = intervalo_rapido
    else:
        intervalo = intervalo_devagar
        
    print('Distancia: {}cm'.format(round(distancia, 2)))
    print('Altura: {}cm'.format(round(altura, 2)))
    print('Velocidade: {}ms'.format(round(intervalo, 2)))

    # Inverta o estado do LED
    LED.value(not LED.value())

# Crie um timer e configure a função de controle do LED para ser chamada periodicamente
timer = Timer(-1)
timer.init(period=intervalo_devagar, mode=Timer.PERIODIC, callback=controlar_led)

# def timer0_callback(timer):
#     global led_state
#     distancia = sensor_distancia.distance_cm()
#     #altura = sensor_altura.distance_cm()
#     #distancia = 42
#     altura = 0;
#     print('Distancia: {}cm'.format(round(distancia, 2)))
#     print('Altura: {}cm'.format(round(altura, 2)))
#     led_pwm = fuzzy_logic(altura,distancia)
#     print('Velocidade: {}ms'.format(round(led_pwm, 2)))
#     if led_pwm != 0:
#         if led_state == 0:
#             LED.value(1)
#             led_state = 1
#         else:
#             LED.value(0)
#             led_state = 0
#         timer0.init(period=led_pwm, mode=Timer.PERIODIC, callback=timer0_callback)  # Double the speed

# timer0 = Timer(0)
# timer0.init(period=500, mode=Timer.PERIODIC, callback=timer0_callback)

