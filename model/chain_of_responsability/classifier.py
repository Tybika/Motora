import joblib
from pathlib import Path
from handler import Handler

class Classifier(Handler):
    def __init__(self):
        super().__init__()
        base = (Path(__file__).resolve().parents[1] / "assets")
        self.cardio = joblib.load(base / "knn_model_cardio.pkl")
        self.cscaler = joblib.load(base / "scaller_cardio.pkl")
        self.flex = joblib.load(base / "knn_model_flex.pkl")
        self.fscaler = joblib.load(base / "scaller_flex.pkl")

    def predict(self, id: str, vector: list):
        if id == "cardio":
            vector = self.cscaler.transform(vector)
            return self.cardio.predict(vector)
        elif id == "flex":
            vector = self.fscaler.transform(vector)
            return self.flex.predict(vector)
        return None
        
    def handle(self, request):
        try:
            vector = request.data["data"]["vector"]
            v_flex = [vector[:5]]
            v_cardio = [vector[:4] + vector[5:]]
            request.data["data"]["class-flex"] = int(self.predict(
                                                "flex", v_flex))
            request.data["data"]["class-cardio"] = int(self.predict(
                                            "cardio", v_cardio))

            request.add_state("classfied")

            if self.next and not request.is_complete():
                return self.next.handle(request)
            else:
                return self.new_response("success", request)
        
        except Exception as e:
            print(e)
            return self.new_response("error", request)