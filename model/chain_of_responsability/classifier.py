import pandas
import joblib
from pathlib import Path
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

import paths
from handler import Handler
from database import Database

class Classifier(Handler):
    def __init__(self):
        super().__init__()
        print("vai vir aí treino do knn vamo ver")
        self.handle()

    def handle(self):
        scaler = StandardScaler()
        db = Database()
        dataframe = pandas.DataFrame(db.get_training("training-cardio"))

        # X = as características, normalizadas e tal
        X = dataframe.drop(columns=["category"])
        X = pandas.get_dummies(X)

        # y = o rótulo 
        y = dataframe["category"]

        # define cada uma dessas variáveis com método próprio
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.25, random_state=42)
        
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        
        knn = KNeighborsClassifier(n_neighbors=5)
        knn.fit(X_train, y_train)

        y_pred = knn.predict(X_test)
        print("Acurácia:", accuracy_score(y_test, y_pred))

        joblib.dump(knn,(Path(__file__).resolve().parents[1] / "assets" / "knn_model_cardio.pkl"))
        joblib.dump(scaler, (Path(__file__).resolve().parents[1] / "assets" / "scaller_cardio.pkl"))



