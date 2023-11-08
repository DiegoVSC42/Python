import time
import random

#Declara as velocidades para piscar o led que posteriormente servirá para apitar um buzzer
intervalo_muito_rapido = 125 #125ms
intervalo_rapido = 250  #250ms
intervalo_devagar = 500 #500ms

#funcoes de pertinencia para o sensor de distancia
#Com 4 conjuntos difusos
def distancia_baixa(x):
    if x <= 10:
        return 1
    return 0
def distancia_media(x):
    if x > 10 and x <= 20:
        return 1
    return 0
def distancia_alta(x):
    if x > 20 and x <= 40:
        return 1
    return 0
def distancia_muito_alta(x):
    if x > 40:
        return 1
    return 0

#funções de pertinencia para sensor de  altura
#Com 4 conjuntos difusos
def altura_baixa(x):
    if x < 10:
        return 1
    return 0
def altura_media(x):
    if x >= 10 and x < 20:
        return 1
    return 0
def altura_alta(x):
    if x >= 20 and x < 40:
        return 1
    return 0
def altura_muito_alta(x):
    if x >= 40:
        return 1
    return 0

# Inferencia Fuzzy
# Calcula o de pertinencia de acordo com a altura e distancia que os sensores obtiveram
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
        #nao pisca ou seja, velocidade = 0
        return(max(altura_baixa(altura),distancia_muito_alta(distancia)))
    
def fuzzy(altura,distancia):
    #Aplica o fuzzy guardando os graus de pertinencia para cada regra
    regras = [
    ("R1", fuzzy_inference(altura,distancia,"R1")),
    ("R2", fuzzy_inference(altura,distancia,"R2")),
    ("R3", fuzzy_inference(altura,distancia,"R3")),
    ("R4", fuzzy_inference(altura,distancia,"R4"))
    ]

    #Mostra qual regra foi escolhida
    print("Regras:", regras)
    
    # Define pesos para cada regra (1 é a mais importante e 0 é a menos importante)
    # A importancia é dada de acordo com a periculosidade, ou seja, a regra R1 seria a referente ao que pode ser mais prejudicial para a vida do utilizador da bengala
    pesos = {
        "R1": 1.0,
        "R2": 0.8,
        "R3": 0.6,
        "R4": 0.4,
    }
    
    return regras, pesos

def defuzzy(regras,peso):
    # Faz a defuzzificação
    defuzzified_value = 0
    total_weight = 0
    for regra, valor in regras:
        peso = pesos[regra]
        defuzzified_value += valor * peso  # Aplique o peso à contribuição da regra
        total_weight += peso  # Atualize o peso total

    if total_weight > 0:
        defuzzified_value /= total_weight  # Calcule a média ponderada

    # Determine o intervalo de piscagem com base na regra que está sendo satisfeita
    if regras[0][1] > 0.7:  # Verifica a regra R1
        intervalo = intervalo_muito_rapido
    elif regras[1][1] > 0.7:  # Verifica a regra R2
        intervalo = intervalo_rapido
    elif regras[2][1] > 0.7:  # Verifica a regra R3
        intervalo = intervalo_devagar
    else:
        intervalo = 0
        
    return intervalo

# funcao periodica 


#altura = sensor_altura.distance_cm() 
altura = random.randint(1,50)
distancia = random.randint(1,50)

while altura != 51:
    altura = int(input("Altura: "))
    distancia = int(input("Distancia: "))
    print("\n")
    regras, pesos = fuzzy(altura,distancia)

    intervalo = defuzzy(regras,pesos)
    
    # Determine o intervalo de piscagem com base na regra que está sendo satisfeita
    if regras[0][1] > 0.7:  # Verifica a regra R1
        intervalo = intervalo_muito_rapido
    elif regras[1][1] > 0.7:  # Verifica a regra R2
        intervalo = intervalo_rapido
    elif regras[2][1] > 0.7:  # Verifica a regra R3
        intervalo = intervalo_devagar
    else:
        intervalo = 0


    print('Distancia: {}cm'.format(round(distancia, 2)))
    print('Altura: {}cm'.format(round(altura, 2)))
    print('Velocidade: {}ms'.format(round(intervalo, 2)))
    print("\n")
