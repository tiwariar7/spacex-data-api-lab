# SpaceX Launch Prediction Dashboard

A full-stack application for analyzing SpaceX launch data and predicting launch success using machine learning.

## Project Structure

- **Flask-Backend/**: Python Flask API with ML model
- **Next-Frontend/**: React/TypeScript frontend with interactive visualizations
- **Notebooks/**: Jupyter notebooks for data analysis and model training

## Quick Start

### 1. Start the Flask Backend

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Notebook**

```bash
cd Next-Frontend
npm install
npm run dev
```

The frontend will run on `http://localhost:5173`

### 3. Access the Application

Open your browser and navigate to `http://localhost:5173` to see the dashboard.

## Key Visualizations

* Interactive maps showing SpaceX launch site locations
* Distance markers between launch sites and nearby infrastructure
* Popups with detailed launch site information
* Lines and circles showing proximity to:

  * Railways
  * Highways
  * Coastlines
  * Cities

## Insights and Analysis

* Launch sites are located near coastlines to ensure safety during rocket launches over open water.
* Proximity to highways and railways suggests considerations for transportation and logistical support.
* A deliberate distance from major urban centers aligns with safety protocols and risk mitigation.
* Visual analysis confirms the strategic selection of launch sites based on geography and accessibility.

## Conclusion

This project demonstrates how spatial visualization can uncover meaningful insights in aerospace logistics. The integration of open-source mapping tools with geospatial data offers a powerful approach to infrastructure and operational planning analysis. The techniques applied here can be extended to other industries and use cases involving geolocation data.

## License

This project is licensed under the [MIT License](LICENSE).
