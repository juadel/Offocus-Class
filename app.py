# app/app.py
# Common python package imports.
from flask import Flask, jsonify, request, render_template
from joblib import load
import numpy as np
# Import from app/features.py.
from features import FEATURES
# Initialize the app and set a secret_key.
app = Flask(__name__)
app.secret_key = 'juancho8'
# Load the pickled model.
model1 = load("KNC_model_all.ml")
model2 = load("KNC_model_MaxVarianceScharr.ml")
model3 = load("KNC_model_VarianceNoise.ml")
model4 = load("KNC_model_VarianceScharr.ml")
@app.route('/api', methods=['GET'])
def api():
    """Handle request and output model score in json format."""
    # Handle empty requests.
    if not request.json:
        return jsonify({'error': 'no request received'})
    # Parse request args into feature array for prediction.
    #x_list, missing_data = parse_args(request.json)
    #x_array = np.array([x_list])
    #print(x_array)
    X_list, missing_data = parse_args(request.json)
    x_array = np.array([X_list])
    print(X_list)
    pred1=int(model1.predict(x_array))
    pred2=int(model2.predict([[X_list[1],X_list[2]]]))
    pred3=int(model3.predict([[X_list[0],X_list[3]]]))
    pred4=int(model4.predict([[X_list[0],X_list[2]]]))
    print(pred1, pred2, pred3, pred4)
    estimate=[pred1, pred2, pred3, pred4]
    print(estimate)
    
    # Predict on x_array and return JSON response.
    #estimate = int(MODEL.predict(x_array))
    response = dict(ESTIMATE=estimate, MISSING_DATA=missing_data)
    return jsonify(response)

def parse_args(request_dict):
    """Parse model features from incoming requests formatted in    
    JSON."""
    # Initialize missing_data as False.
    missing_data = False
# Parse out the features from the request_dict.
    x_list = []
    for feature in FEATURES:
        value = request_dict.get(feature, None)
        if value:
            x_list.append(value)
        else:# Handle missing features.
        	 x_list.append(0)
        	 missing_data = True 
    return x_list, missing_data


if __name__ == '__main__':
 	app.run(host='0.0.0.0', port=5000, debug=True)
