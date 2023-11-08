# Funções de pertinência para a temperatura
def temperatura_baixa(x):
    if x <= 20:
        return 1
    elif x > 20 and x < 25:
        return (25 - x) / 5
    else:
        return 0

def temperatura_media(x):
    if x >= 20 and x <= 25:
        return (x - 20) / 5
    elif x > 25 and x < 30:
        return (30 - x) / 5
    else:
        return 0

def temperatura_alta(x):
    if x >= 30:
        return 1
    elif x > 25 and x < 30:
        return (x - 25) / 5
    else:
        return 0

# Funções de pertinência para a velocidade do ventilador
def velocidade_baixa(x):
    if x <= 30:
        return 1
    elif x > 30 and x < 60:
        return (60 - x) / 30
    else:
        return 0

def velocidade_media(x):
    if x >= 30 and x <= 60:
        return (x - 30) / 30
    elif x > 60 and x < 90:
        return (90 - x) / 30
    else:
        return 0

def velocidade_alta(x):
    if x >= 90:
        return 1
    elif x > 60 and x < 90:
        return (x - 60) / 30
    else:
        return 0

# Inferência Fuzzy
def fuzzy_inference(temperatura, regra):
    if regra == "R1":
        return min(temperatura_baixa(temperatura), velocidade_alta(temperatura))
    elif regra == "R2":
        return min(temperatura_media(temperatura), velocidade_media(temperatura))
    elif regra == "R3":
        return min(temperatura_alta(temperatura), velocidade_baixa(temperatura))

# Definição da temperatura e regras
temperatura = 28  # Exemplo de temperatura
regras = [("R1", fuzzy_inference(temperatura, "R1")),
          ("R2", fuzzy_inference(temperatura, "R2")),
          ("R3", fuzzy_inference(temperatura, "R3"))]

# Agregação das saídas fuzzy
defuzzified_value = 0
total_weight = 0
for regra, valor in regras:
    defuzzified_value += valor * fuzzy_inference(temperatura, regra)
    total_weight += valor

if total_weight > 0:
    defuzzified_value /= total_weight

print(f"Temperatura: {temperatura}°C")
print(f"Velocidade do Ventilador: {defuzzified_value}%")