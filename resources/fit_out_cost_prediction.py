
from flask import jsonify, Blueprint, request

from flask_restful import Resource, Api
from sklearn.externals import joblib
from services.cost_prediction_failed import CostPredictionFailed

costPredictionModel = joblib.load(
    "./deep_learning_models/LR_33%split_model_inc_CatAB.pkl")


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

            cost = costPredictionModel.predict(
                [costPredictionParametersForModel])[0]

        except ValueError as error:
            return jsonify({'error': 'some error message'})
        
        except TypeError as error:
            raise CostPredictionFailed(error.args[0], response_status_code=500)

        except KeyError as error:
            return jsonify({'error': 'some error message'})

        # return a json value
        return jsonify({'cost': cost})


fitout_cost_prediction_api = Blueprint(
    'resources.fit_out_cost_prediction', __name__)

api = Api(fitout_cost_prediction_api)
api.add_resource(
    FitOutCostPrediction,
    '/fitOutCostPrediction',
    endpoint='fitOutCostPrediction'
)
