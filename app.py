from flask import Flask,abort,jsonify,request
import numpy as np
from sklearn.externals import joblib
from flask_cors import CORS


model = joblib.load("./LR_33%split_model_inc_CatAB.pkl")

#creating web service running on port 8000, answer POST requests
app = Flask(__name__)
cors = CORS(app, resources={
  r"/*": {
    "origins": ["https://testing-cost-predictor.firebaseapp.com", "https://frontend-cost-predictor-ac557.firebaseapp.com"]
  }
})

@app.route("/fitOutCostPrediction", methods=['POST'])

#prediction function
def make_predict():

    if request.method =='POST':
        try:
            costPredictionParameters = request.get_json()
            buildingVolume = costPredictionParameters['buildingVolume']
            isCatAIncluded = 0
            isCatBIncluded = 0
            isCatAAndBIncluded = 0

            if costPredictionParameters['isCatAIncluded'] == true:
                isCatAIncluded = 1
            if costPredictionParameters['isCatBIncluded'] == true:
                isCatBIncluded = 1
            if costPredictionParameters['isCatAIncluded'] == true and costPredictionParameters['isCatBIncluded'] == true:
                isCatAAndBIncluded = 1
            
            costPredictionParametersForModel = {
                'volume':buildingVolume, 
                'cat_type_A':isCatAIncluded, 
                'cat_type_B':isCatBIncluded, 
                'cat_type_AB':isCatAAndBIncluded
            } 

            a = input(costPredictionParametersForModel)
            cost_pred = model.predict([a])[0] 
       
        except ValueError:
            return jsonify("error text here")
        
        # return a json value
        return json.dumps({'cost':cost_pred})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
