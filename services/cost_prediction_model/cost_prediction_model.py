
from sklearn.externals import joblib

class CostPredictionModel:
    def __init__(self):
       self.costPredictionModel = joblib.load(
          "./services/cost_prediction_model/LR_split_model_MASTER_8thAugust.pkl")

    def predictCost(self, costPredictionParametersForModel):
        return self.costPredictionModel.predict(
                [costPredictionParametersForModel])[0]
