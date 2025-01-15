from flask import Flask, render_template, request, redirect, url_for, jsonify
import pickle
import numpy as np

app = Flask(__name__)


with open('Random_forest_model1.pkl', 'rb') as file:
    random_forest_model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    try:
        data = request.json
        
        # Create feature array in the correct order
        features = np.array([[
            data['age'],
            data['serum_creatine'],
            data['blood_pressure'],
            data['blood_urea'],
            data['haemoglobin'],
            data['albumin'],
            data['blood_glucose_random'],
            data['potassium'],
            data['anemia'],
            data['hypertension']
        ]])

        # Make prediction
        prediction = random_forest_model.predict(features)

        # Map prediction to output text
        if prediction[0] == 1:
            result = "CKD Detected"
        else:
            result = "No CKD Detected"

        return jsonify({'result': result})
    
    except Exception as e:
        return jsonify({'error' : str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)