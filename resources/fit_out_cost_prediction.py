
from flask import jsonify, Blueprint, json, request, json

from flask_restful import Resource, Api
from sklearn.externals import joblib

model = joblib.load("./deep_learning_models/LR_33%split_model_inc_CatAB.pkl")


class FitOutCostPrediction(Resource):
    def post(self):
        try:
            costPredictionParameters = request.get_json()
            buildingVolume = costPredictionParameters['buildingVolume']
            isCatAIncluded = 0
            isCatBIncluded = 0
            isCatAAndBIncluded = 0

            if costPredictionParameters['isCatAIncluded'] == True and costPredictionParameters['isCatBIncluded'] == True:
                isCatAAndBIncluded = 1
            elif costPredictionParameters['isCatAIncluded'] == True and costPredictionParameters['isCatBIncluded'] == False:
                isCatAIncluded = 1
            elif costPredictionParameters['isCatAIncluded'] == False and costPredictionParameters['isCatBIncluded'] == True:
                isCatBIncluded = 1

            costPredictionParametersForModel = [
                buildingVolume, isCatAIncluded, isCatBIncluded, isCatAAndBIncluded]

            cost = model.predict([costPredictionParametersForModel])[0]

        except ValueError:
            return jsonify("error text here")

        # return a json value
        return json.dumps({'cost': cost})


fitout_cost_prediction_api = Blueprint(
    'resources.fit_out_cost_prediction', __name__)

api = Api(fitout_cost_prediction_api)
api.add_resource(
    FitOutCostPrediction,
    '/fitOutCostPrediction',
    endpoint='fitOutCostPrediction'
)
