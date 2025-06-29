from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model
with open('ML-Model/spacex_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the SpaceX dataset
df = pd.read_csv('ML-Model/datasets/spacex_launch_dataset.csv')

# Feature names expected by the model (based on actual training)
# The model was trained with: PayloadMass + LaunchSite (one-hot encoded with drop_first=True)
FEATURE_NAMES = [
    'PayloadMass',
    'LaunchSite_CCAFS SLC 40',  # This is the first category after drop_first=True
    'LaunchSite_KSC LC 39A',
    'LaunchSite_VAFB SLC 4E'
]

def preprocess_input_data(data):
    """
    Preprocess input data to match the model's expected format
    """
    # Create a DataFrame from the input data
    input_df = pd.DataFrame([data])
    
    # Map launch sites to match the dataset format
    launch_site_mapping = {
        'CCAFS LC-40': 'CCAFS SLC 40',  # Map to dataset format
        'CCAFS SLC-40': 'CCAFS SLC 40', 
        'KSC LC-39A': 'KSC LC 39A',
        'VAFB SLC-4E': 'VAFB SLC 4E'
    }
    
    # Apply launch site mapping
    if 'Launch Site' in input_df.columns:
        input_df['LaunchSite'] = input_df['Launch Site'].replace(launch_site_mapping)
        input_df = input_df.drop('Launch Site', axis=1)
    
    # Rename Payload Mass to match model expectations
    if 'Payload Mass (kg)' in input_df.columns:
        input_df['PayloadMass'] = input_df['Payload Mass (kg)']
        input_df = input_df.drop('Payload Mass (kg)', axis=1)
    
    # Remove Booster Version Category as it's not used in the model
    if 'Booster Version Category' in input_df.columns:
        input_df = input_df.drop('Booster Version Category', axis=1)
    
    # One-hot encode LaunchSite (same as training)
    input_df = pd.get_dummies(input_df, columns=['LaunchSite'], drop_first=True)
    
    # Ensure all expected features are present
    for feature in FEATURE_NAMES:
        if feature not in input_df.columns:
            input_df[feature] = 0
    
    # Reorder columns to match training data
    input_df = input_df[FEATURE_NAMES]
    
    return input_df

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from request
        data = request.json
        
        # Preprocess the input data
        input_df = preprocess_input_data(data)
        
        # Make prediction
        prediction = model.predict(input_df)
        probability = model.predict_proba(input_df)
        
        # Return prediction
        return jsonify({
            'prediction': int(prediction[0]),
            'probability': float(probability[0][1]),  # probability of success
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 400

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

@app.route('/launches', methods=['GET'])
def get_launches():
    try:
        # Convert the dataset to the format expected by the frontend
        launches = []
        
        for index, row in df.iterrows():
            # Map the Class column to success (1 = success, 0 = failure)
            success = bool(row['Class'])
            
            # Map launch sites to match frontend expectations
            launch_site_mapping = {
                'CCAFS SLC 40': 'CCAFS SLC-40',
                'KSC LC 39A': 'KSC LC-39A',
                'VAFB SLC 4E': 'VAFB SLC-4E'
            }
            
            launch_site = launch_site_mapping.get(str(row['LaunchSite']), str(row['LaunchSite']))
            
            # Map booster versions to match frontend expectations
            booster_version_mapping = {
                'Falcon 9': 'Falcon 9 B5',
                'Falcon 9 v1.0': 'Falcon 9 v1.0',
                'Falcon 9 v1.1': 'Falcon 9 v1.1'
            }
            
            booster_version = booster_version_mapping.get(str(row['BoosterVersion']), str(row['BoosterVersion']))
            
            launch_data = {
                "id": str(row['FlightNumber']),
                "flightNumber": int(row['FlightNumber']),
                "missionName": f"Flight {row['FlightNumber']}",  # Generate mission name if not available
                "launchSite": launch_site,
                "payloadMass": float(row['PayloadMass']),
                "success": success,
                "boosterVersion": booster_version,
                "launchDate": row['Date']
            }
            launches.append(launch_data)
        
        return jsonify(launches)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)