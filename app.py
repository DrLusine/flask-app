from flask import Flask,abort,jsonify,request,json
import numpy as np
from sklearn.externals import joblib
from flask_cors import CORS


model = joblib.load("./LR_33%split_model_inc_CatAB.pkl")

#creating web service running on port 8000, answer POST requests
app = Flask(__name__)   
cors = CORS(app, resources={
  r"/*": {
    "origins": ["https://testing-cost-predictor.firebaseapp.com","http://localhost:9000", "https://frontend-cost-predictor-ac557.firebaseapp.com"]
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

            if costPredictionParameters['isCatAIncluded'] == True and costPredictionParameters['isCatBIncluded'] == True:
                isCatAAndBIncluded = 1
            elif costPredictionParameters['isCatAIncluded'] == True and costPredictionParameters['isCatBIncluded'] == False:
                isCatAIncluded = 1
            elif costPredictionParameters['isCatAIncluded'] == False and costPredictionParameters['isCatBIncluded'] == True:
                isCatBIncluded = 1
            
            costPredictionParametersForModel = [buildingVolume, isCatAIncluded, isCatBIncluded, isCatAAndBIncluded]
            
            cost = model.predict([costPredictionParametersForModel])[0]
       
        except ValueError:
            return jsonify("error text here")
        
        # return a json value
        return json.dumps({'cost':cost})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
