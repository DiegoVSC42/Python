from machine import Pin, PWM
import time

# Configurar o pino GPIO para o controle do buzzer
buzzer_pin = 12
buzzer = PWM(Pin(12), freq=440*6, duty=0)  # freq é a frequência em Hz

# Função para tocar o buzzer
def tocar_buzzer(intervalo):
    # Ativar o buzzer
    buzzer.duty(500)  # ajuste o valor conforme necessário
    time.sleep(intervalo / 1000.0)  # converter para segundos
    buzzer.duty(0)

# Chamar a função para tocar o buzzer
tocar_buzzer(10000)
