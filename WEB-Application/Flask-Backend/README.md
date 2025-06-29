# Flask Backend for SpaceX Launch Prediction

This Flask backend provides APIs for SpaceX launch data and predictions using a trained machine learning model.

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Make sure the ML model file exists:
- `ML-Model/spacex_model.pkl` - The trained machine learning model
- `ML-Model/datasets/spacex_launch_dataset.csv` - The SpaceX launch dataset

## Running the Backend

```bash
python app.py
```

The server will start on `http://localhost:5000`

## API Endpoints

- `GET /health` - Health check endpoint
- `GET /launches` - Get all historical launch data
- `POST /predict` - Make a launch success prediction

### Prediction Endpoint

Send a POST request to `/predict` with the following JSON format:

```json
{
  "Payload Mass (kg)": 5000,
  "Launch Site": "KSC LC-39A",
  "Booster Version Category": "Falcon 9 B5"
}
```

Response:
```json
{
  "prediction": 1,
  "probability": 0.85,
  "status": "success"
}
```

## CORS

CORS is enabled to allow requests from the Next.js frontend running on a different port.