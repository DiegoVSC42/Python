import pandas as pd

dados = {
    "Eixo_X": [1, 1.5, 2, 1.5, -1, -0.5, 0, -0.5],
    "Eixo_Y": [1, 1.5, 1, 0.5, -1, -0.5, -1, -1.5],
    "Cor": [1, 1, 1, 1, 0, 0, 0, 0],
}

df = pd.DataFrame(dados)
df.to_csv("dados.csv", index=False)
