
from sklearn.externals import joblib

class CostPredictionModel:
    def __init__(self):
       self.costPredictionModel = joblib.load(
          "./services/cost_prediction_model/LR_33%split_model_inc_CatAB.pkl")

    def predictCost(self, costPredictionParametersForModel):
        return self.costPredictionModel.predict(
                [costPredictionParametersForModel])[0]