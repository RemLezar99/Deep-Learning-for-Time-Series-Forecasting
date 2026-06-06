# Deep-Learning-for-Time-Series-Forecasting
Can a deep learning model forecast future values better than simple statistical or naive baselines?

In this project, we build a time-series forecasting system for bike rental demand using naive baselines, classical ML, and deep learning models, then deploy an interactive Streamlit dashboard to visualize forecasts and model errors.

# Bike Demand Forecasting

This project explores time-series forecasting for bike rental demand using historical demand, calendar features, and weather-related variables.

The goal is to compare simple forecasting baselines, classical machine learning models, and deep learning sequence models such as LSTMs or GRUs. The project will also include a small Streamlit web frontend for visualizing forecasts, model predictions, and evaluation results.

## Planned features

- Exploratory data analysis of bike rental demand patterns
- Chronological train/validation/test split
- Naive forecasting baselines
- Classical machine learning baseline
- Deep learning forecasting model using LSTM or GRU
- Model evaluation using MAE and RMSE
- Streamlit dashboard for visualizing predictions

## Project structure

```text
bike-demand-forecasting/
├── app/                 # Streamlit frontend
├── data/
│   ├── raw/             # Raw dataset files, not committed
│   └── processed/       # Processed dataset files, not committed
├── models/              # Trained model artifacts, not committed
├── notebooks/           # Exploratory and modeling notebooks
├── results/
│   └── figures/         # Metrics, prediction files, and generated figures
├── src/                 # Reusable Python source code
├── .gitignore
├── README.md
└── requirements.txt
```

## Setup

Create a virtual environment:
```
python -m venv .venv
```
Activate it:

### macOS/Linux
```
source .venv/bin/activate
```
### Windows PowerShell
```
.venv\Scripts\Activate.ps1
```
Install dependencies:
```
pip install --upgrade pip
pip install -r requirements.txt
```
Add the virtual environment as a Jupyter kernel:
```
python -m ipykernel install --user --name bike-demand-forecasting --display-name "Python (bike-demand-forecasting)"
```
Run Jupyter:
```
jupyter notebook
```
Run the Streamlit app, once it exists:
```
streamlit run app/streamlit_app.py
```
## Data
The dataset has not been selected yet. Raw data files should be placed in:
```
data/raw/
```
Processed files should be saved to:
```
data/processed/
```
Large data files should not be committed to Git.