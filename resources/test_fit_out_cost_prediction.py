from flask import Flask, jsonify, json
from resources.fit_out_cost_prediction import fitout_cost_prediction_api
from numbers import Number
from unittest.mock import patch
import pytest

@pytest.fixture
def prediction_test_params():
    predictionTestParams = {
        'floorArea': {
            'areaValue': 10000,
            'areaUnit': 'sq_ft'
        },
        'averageFloorHeight': {
            'heightValue': 3,
            'heightUnit': 'm'
        },
        'isCatAIncluded': False,
        'isCatBIncluded': True
    }
    return predictionTestParams


def test_fit_out_cost_prediction_with_areainsqft_heightinmetres(test_client_factory, prediction_test_params):
    client = test_client_factory(fitout_cost_prediction_api)

    response = client.post('/fitOutCostPrediction', json=prediction_test_params)

    assert response.status_code == 200
    response_data = response.get_json()
    assert isinstance(response_data['cost'], Number)

def test_fit_out_cost_prediction_with_areainsqmetres_heightinfeet(test_client_factory, prediction_test_params):
    client = test_client_factory(fitout_cost_prediction_api)

    prediction_test_params['averageFloorHeight']['heightUnit'] = 'ft'
    prediction_test_params['averageFloorHeight']['areaUnit'] = 'sq_m'
    
    response = client.post('/fitOutCostPrediction', json=prediction_test_params)

    assert response.status_code == 200
    response_data = response.get_json()
    assert isinstance(response_data['cost'], Number)