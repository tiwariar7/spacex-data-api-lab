# SpaceX Launch Prediction Dashboard

A full-stack application for analyzing SpaceX launch data and predicting launch success using machine learning.

## Project Structure

- **Flask-Backend/**: Python Flask API with ML model
- **Next-Frontend/**: React/TypeScript frontend with interactive visualizations
- **Notebooks/**: Jupyter notebooks for data analysis and model training

## Quick Start

### 1. Start the Flask Backend

```bash
cd Flask-Backend
pip install -r requirements.txt
python app.py
```

The backend will run on `http://localhost:5000`

### 2. Start the Next.js Frontend

In a new terminal:

```bash
cd Next-Frontend
npm install
npm run dev
```

The frontend will run on `http://localhost:5173`

### 3. Access the Application

Open your browser and navigate to `http://localhost:5173` to see the dashboard.

## Features

- **Interactive Dashboard**: Filter and visualize SpaceX launch data
- **Machine Learning Predictions**: Real-time launch success predictions
- **Data Visualization**: Pie charts and scatter plots
- **Historical Analysis**: Complete SpaceX launch history

## API Endpoints

- `GET /health` - Health check
- `GET /launches` - Get all launch data
- `POST /predict` - Make launch predictions

## Technologies Used

- **Backend**: Flask, scikit-learn, pandas
- **Frontend**: React, TypeScript, Vite, Tailwind CSS
- **Visualization**: Chart.js
- **ML Model**: Trained on SpaceX historical data

## Data Sources

The application uses the SpaceX launch dataset containing:
- Launch success/failure data
- Payload mass information
- Launch site details
- Booster version information
- Historical flight data

## Development

### Backend Development
- Located in `Flask-Backend/`
- Uses the trained model from `ML-Model/spacex_model.pkl`
- Serves data from `ML-Model/datasets/spacex_launch_dataset.csv`

### Frontend Development
- Located in `Next-Frontend/`
- Built with Vite for fast development
- Uses TypeScript for type safety
- Responsive design with Tailwind CSS

## Troubleshooting

<<<<<<< HEAD
1. **Backend won't start**: Make sure all Python dependencies are installed
2. **Frontend can't connect to backend**: Ensure the Flask server is running on port 5000
3. **CORS errors**: The backend has CORS enabled, but check if the frontend is making requests to the correct URL
4. **ML model errors**: Verify that `spacex_model.pkl` exists in the ML-Model directory
=======
4. **Launch the Notebook**

   ```bash
   jupyter notebook
   ```

   Open the provided `.ipynb` file and follow the step-by-step analysis.

## Key Visualizations

* Interactive maps showing SpaceX launch site locations
* Distance markers between launch sites and nearby infrastructure
* Popups with detailed launch site information
* Lines and circles showing proximity to:

  * Railways
  * Highways
  * Coastlines
  * Cities





## License

This project is licensed under the [MIT License](LICENSE).
>>>>>>> 7f2c4a98ae0022e53b64a364e95c1fa3b2fe0d4f
