# Algoritmo para mostrar acuracia do método de machine learning da árvore de decisão

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score

df = pd.read_csv("creditos.csv")

negative_age_indices = df[df["age"] < 0].index
positive_age_mean = df[df["age"] >= 0]["age"].mean()
df.loc[negative_age_indices, "age"] = positive_age_mean

X = df[["income", "age", "loan"]]
y = df["default"]

imputer = SimpleImputer(strategy="mean")
X = imputer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)
dt_pred = dt_model.predict(X_test)

dt_accuracy = accuracy_score(y_test, dt_pred)
dt_accuracy = dt_accuracy * 100
print("Acurácia da Árvore de Decisão: ", dt_accuracy, "%")
