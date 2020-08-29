import pickle
import flask
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

def load_models():
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

@app.route('/predict', methods=['GET'])
def predict():
    # stub input features
    # parse input features from request
    #request_json = request.get_json()
    #x = float(request_json['input'])

    args = request.args
    x = float(args['input'])
    # load model
    model = load_models()
    prediction = model.predict([[x]])[0]
    response = json.dumps({'response': prediction})
    return response, 200

if __name__ == '__main__':
    app.run(debug=True)