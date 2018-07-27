from flask import Flask, abort, jsonify, request, json
import numpy as np
from sklearn.externals import joblib
from flask_cors import CORS
from resources.fit_out_cost_prediction import fitout_cost_prediction_api

DEBUG = True
HOST = '0.0.0.0'
PORT = 8080

app = Flask(__name__)

app.register_blueprint(fitout_cost_prediction_api)

cors = CORS(app, resources={
    r"/*": {
        "origins": ["https://testing-cost-predictor.firebaseapp.com", "http://localhost:9000", "https://frontend-cost-predictor-ac557.firebaseapp.com"]
    }
})

if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
