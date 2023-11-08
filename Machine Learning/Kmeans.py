# Importando o pandas
import pandas as pd

# Usando a base de dados abaixo
dados = {
    "A": [1, 1.5, 2, 1.5, -1, -0.5, 0, -0.5],
    "A2": [-0.5, 0, -0.5, -1, 1.5, 2, 1.5, 1],
    "B": [1, 1.5, 1, 0.5, -1, -0.5, -1, -1.5],
    "B2": [-1.5, -1, -0.5, -1, 0.5, 1, 1.5, 1],
    "y": [1, 1, 1, 1, 0, 0, 0, 0],
    "y2": [0, 0, 0, 0, 1, 1, 1, 1],
}

dados = pd.DataFrame(dados)

# E esses dados para fazer a previsão
dados_pred = {
    "A": [2.5, 1.8, 0.5, -1, -1],
    "B": [2, 1, 0, 0, -1.5],
    "A2": [2.5, 1.8, 0.5, -1, -1],
    "B2": [2, 1, 0, 0, -1.5],
}

dados_pred = pd.DataFrame(dados_pred)

# Podemos visualizar graficamente esses pontos
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.scatter(x=dados.A, y=dados.B, c=dados.y, cmap="viridis")
ax.scatter(x=dados_pred.A, y=dados_pred.B, c="r", marker="s")

plt.show()

# Importando o KNN
from sklearn.neighbors import KNeighborsClassifier

# Criando o classificador
clf = KNeighborsClassifier(n_neighbors=3)

# Selecionando os pontos de treino
X = dados[["A2", "B2"]]
y = dados.y2

# E agora selecionando os dados de teste
X_test = dados_pred[["A2", "B2"]]

# Podemos fazer o fit com os dados de treino
clf = clf.fit(X, y)

# E a previsão para os dados de teste
y_pred = clf.predict(X_test)

# Podemos incluir nos dados de treino, a visualização dos dados de teste
fig, ax = plt.subplots()

ax.scatter(x=dados.A, y=dados.B, c=dados.y, cmap="viridis")
ax.scatter(x=dados_pred.A, y=dados_pred.B, c=y_pred, marker="s")

plt.show()

# Podemos visualizar os dados que usamos anteriormente
dados[["A2", "B2", "y2"]]

# Importando o dataset e o pandas
from sklearn.datasets import load_iris

# Retornando os dados
iris = load_iris()
iris

# Transformando em um DataFrame
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df["target"] = iris.target

# Visualizando a base
iris_df

# Selecionando apenas as colunas de pétala
iris1 = iris_df.loc[
    iris_df.target.isin([1, 2]), ["petal length (cm)", "petal width (cm)", "target"]
]
iris1

# Separando X e y
X = iris1[["petal length (cm)", "petal width (cm)"]]
y = iris1.target

# Fazendo o train_test_split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)

# Visualizando os dados de treino
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.scatter(
    x=X_train["petal width (cm)"],
    y=X_train["petal length (cm)"],
    c=y_train,
    cmap="viridis",
)

ax.set(xlim=(0.9, 2.6), xticks=[1, 1.5, 2, 2.5], ylim=(3, 7), yticks=[3, 4, 5, 6, 7])

plt.show()

# Importando o KNN
from sklearn.neighbors import KNeighborsClassifier

# Criando o classificador
clf = KNeighborsClassifier(n_neighbors=3)

# Fazendo o fit com os dados de treino
clf = clf.fit(X_train, y_train)

# Fazendo a previsão para os dados de teste
y_pred = clf.predict(X_test)

# Verificando a matriz de confusão
from sklearn.metrics import confusion_matrix

confusion_matrix(y_test, y_pred)

# Podemos agora visualizar os dados de treino e teste
fig, ax = plt.subplots()

ax.scatter(
    x=X_train["petal width (cm)"],
    y=X_train["petal length (cm)"],
    c=y_train,
    alpha=0.7,
    cmap="viridis",
)
ax.scatter(
    x=X_test["petal width (cm)"],
    y=X_test["petal length (cm)"],
    c=y_pred,
    alpha=0.2,
    cmap="RdYlGn",
)
ax.scatter(
    x=X_test["petal width (cm)"],
    y=X_test["petal length (cm)"],
    c=y_test,
    alpha=0.2,
    cmap="RdYlGn",
)

ax.set(xlim=(0.9, 2.6), xticks=[1, 1.5, 2, 2.5], ylim=(3, 7), yticks=[3, 4, 5, 6, 7])

plt.show()

X_test[y_test != y_pred]
