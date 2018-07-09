from flask import Flask,abort,jsonify,request
import numpy as np
from sklearn.externals import joblib
from flask_cors import CORS


model = joblib.load("./LM_33%_split_model_python3.pkl")

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
            #expecting user imput as a json file with a title 'volume'
             data=request.form      
                 volume = data['volume']
                 catA = data['cat_a']
                 catB = data['cat_b']
                 catAandB = data['cat_a_b'] 
             user_data={'volume':volume, 'cat_a':catA, 'cat_b':catB,'cat_a_b':catAandB} 
             a = input(user_data)
             cost_pred = model.predict([a])[0] 
       
      except ValueError:
            return jsonify("error text here")
        
        # return a json value
        return json.dumps({'cost':cost_pred});
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
