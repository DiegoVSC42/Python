import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
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

knn_model = KNeighborsClassifier(n_neighbors=5)

knn_model.fit(X_train, y_train)

knn_pred = knn_model.predict(X_test)

knn_accuracy = accuracy_score(y_test, knn_pred)
knn_accuracy = knn_accuracy * 100

print("Acurácia do KNN: ", knn_accuracy, "%")
