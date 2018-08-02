from flask import jsonify
from app import app
from services.error_handling.exceptions.cost_prediction_failed import CostPredictionFailed

@app.errorhandler(CostPredictionFailed)
def handle_cost_prediction_failed(error):
    return error.get_http_error_response()