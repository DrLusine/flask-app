
from flask import Flask
from flask_cors import CORS
import pytest
from services.cost_prediction_failed import CostPredictionFailed

@pytest.fixture
def app_instance():
    app = Flask(__name__)
    app.config['TESTING'] = True

    @app.errorhandler(CostPredictionFailed)
    def handle_cost_prediction_failed(error):
        return error.get_http_error_response()

    return app
