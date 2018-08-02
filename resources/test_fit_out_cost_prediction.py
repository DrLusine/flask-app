from flask import Flask, jsonify
from resources.fit_out_cost_prediction import fitout_cost_prediction_api
from numbers import Number
from unittest.mock import patch
import pytest


def test_get_fit_out_cost_prediction(test_client_factory):
        mockCostPredictionModel = patch('services.cost_prediction_model.cost_prediction_model.CostPredictionModel')
        mockCostPredictionModel.return_value = 2.5738289898977080
        client = test_client_factory(fitout_cost_prediction_api)

        response = client.post('/fitOutCostPrediction', json=
        {
        'buildingVolume': 1000,
        'isCatAIncluded': False, 
        'isCatBIncluded': True
        })
        
        assert response.status_code == 200
        response_data = response.get_json()
        assert isinstance(response_data['cost'], Number)

'''def test_convert_volume_to_cubic_meters(test_client_factory):
        client = test_client_factory(fitout_cost_prediction_api)

        response = client.post('/fitOutCostPrediction', json=
        {
        'buildingVolume': 
                {
                'buildingVolumeValue': 10000, 
                'buildingVolumeUnit': 'cubic foot'
                }, 
        'isCatAIncluded': False, 
        'isCatBIncluded': True
        })
        
        assert response.status_code == 200
        response_data = response.get_json()
        assert isinstance(response_data['cost'], Number)'''