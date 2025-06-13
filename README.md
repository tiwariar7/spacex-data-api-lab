# SpaceX Data API Lab

This repository contains a hands-on data engineering and data preprocessing lab focused on collecting and preparing data from the SpaceX public API and Wikipedia. The project is part of a Falcon 9 Launch Analysis and aims to enable further exploratory data analysis and machine learning workflows.

## Overview

The objective of this lab is to:

* Retrieve and parse launch data using the official SpaceX REST API.
* Scrape supplementary launch data from Wikipedia for Falcon 9 and Falcon Heavy missions.
* Structure, clean, and transform the data into Pandas DataFrames.
* Prepare a consolidated dataset for analysis, visualization, or predictive modeling.

## Data Sources

1. **SpaceX REST API (v5)**
   Endpoint: `https://api.spacexdata.com/v5/launches`
   Returns detailed metadata for each launch, including payloads, cores, launch sites, and success status.

2. **Wikipedia Falcon Launch History**
   Web-scraped using BeautifulSoup from:
   [List of Falcon 9 and Falcon Heavy launches](https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches)
   This data includes mission details, rocket types, outcomes, and launch dates.

## Repository Contents

```
spacex-data-api-lab/
│
├── README.md                  # Project documentation
├── spacex_data_lab.ipynb      # Jupyter notebook with step-by-step data collection
└── spacex_data_collection.py  # Python script for API and web scraping operations
```

## Setup and Requirements

Install required Python packages:

```bash
pip install requests pandas beautifulsoup4
```

Alternatively, set up a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `requirements.txt` file with the following contents if not present:

```
requests
pandas
beautifulsoup4
```

## How to Use

1. **Clone the Repository**

```bash
git clone https://github.com/tiwariar7/spacex-data-api-lab.git
cd spacex-data-api-lab
```

2. **Run the Script or Notebook**

* To run the script:

  ```bash
  python spacex_data_collection.py
  ```

* To run interactively:

  ```bash
  jupyter notebook spacex_data_lab.ipynb
  ```

3. **Output**

Both API and Wikipedia data will be loaded into separate Pandas DataFrames. You may optionally export them as CSV files for future use.

## Features

* RESTful API data ingestion
* HTML table scraping and parsing
* Data cleanup, formatting, and normalization
* Modular Python functions for reusable data collection workflows

## Use Cases

This lab is a foundational step for:

* Predictive modeling (e.g., first-stage landing success)
* Exploratory data analysis (e.g., launch trends, reuse frequency)
* Building interactive dashboards or visual reports
* Enriching datasets by combining structured and semi-structured sources

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

* [SpaceX](https://github.com/r-spacex/SpaceX-API) for providing the public API.
* Wikipedia contributors for maintaining an extensive launch history.

---
