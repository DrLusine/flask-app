from flask import Flask, jsonify
from numbers import Number
from resources.fit_out_cost_prediction import fitout_cost_prediction_api
import pytest


def test_get_fit_out_cost_prediction(app_instance):
        app_instance.register_blueprint(fitout_cost_prediction_api)
        client = app_instance.test_client()
        response = client.post('/fitOutCostPrediction', json={
        'buildingVolume': 10000, 'isCatAIncluded': False, 'isCatBIncluded': True
    })
        assert response.status_code == 200
        response_data = response.get_json()
        assert isinstance(response_data['cost'], Number)