# My_software_development_project
# Vehicle Data Explorer

## Overview
This project is a **Streamlit web app** that allows users to explore and analyze a dataset of used vehicles. It provides **interactive visualizations** using Plotly and Pandas to help users gain insights into pricing, mileage, and other factors affecting vehicle listings.

## Features
- **Interactive scatter plots** to explore the relationship between price and odometer readings.
- **Dataset preview** to view the first few rows of the dataset.
- **Checkbox toggles** for displaying different components.

## Technologies Used
- **Python**
- **Pandas** (for data manipulation)
- **Plotly Express** (for visualizations)
- **Streamlit** (for the interactive web app)

## How to Install & Run Locally

1. **Clone the Repository** (if sharing via GitHub):
   ```bash
   git clone <your-github-repo-url>
   cd My_software_development_project

python3 -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows

pip install -r requirements.txt

streamlit run app.py

