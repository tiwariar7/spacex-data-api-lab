# SpaceX Launch Site Visualization using Folium

This repository contains a geospatial data analysis and visualization project focused on SpaceX launch sites. Using Python and the Folium mapping library, the project visualizes launch site locations and evaluates their geographic proximity to critical infrastructure such as highways, railways, coastlines, and urban areas.

## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Installation and Setup](#installation-and-setup)
- [Project Structure](#project-structure)
- [Key Visualizations](#key-visualizations)
- [Insights and Analysis](#insights-and-analysis)
- [Conclusion](#conclusion)
- [License](#license)
- [Author](#author)

## Overview

The success and safety of aerospace missions are heavily influenced by the geographical attributes of launch sites. This project explores the spatial characteristics of SpaceX launch facilities to understand their placement strategies. The visualizations generated offer insight into why these locations were chosen and how they align with operational and logistical requirements.

## Technologies Used

- Python 3.8+
- Folium (for interactive map visualization)
- Pandas (for data processing)
- Geopy (for distance calculations)
- Jupyter Notebook (for exploratory analysis and development)

## Installation and Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/tiwariar7/spacex-launch-site-visualization.git
   cd spacex-launch-site-visualization
   ```

2. **Create and Activate a Virtual Environment (Optional)**

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

## Insights and Analysis

* Launch sites are located near coastlines to ensure safety during rocket launches over open water.
* Proximity to highways and railways suggests considerations for transportation and logistical support.
* A deliberate distance from major urban centers aligns with safety protocols and risk mitigation.
* Visual analysis confirms the strategic selection of launch sites based on geography and accessibility.

## Conclusion

This project demonstrates how spatial visualization can uncover meaningful insights in aerospace logistics. The integration of open-source mapping tools with geospatial data offers a powerful approach to infrastructure and operational planning analysis. The techniques applied here can be extended to other industries and use cases involving geolocation data.

## License

This project is licensed under the [MIT License](LICENSE).
