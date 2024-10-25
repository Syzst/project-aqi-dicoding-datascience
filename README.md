# Guanyuan Air Quality Dashboard 🌍

This project provides a dashboard for analyzing air quality data in Guanyuan (2013-2017), including pollutant levels, wind speed/direction effects, and correlations between various pollutants.

## Setup Environment

### Option 1: Using Anaconda

If you prefer using Anaconda, follow the steps below:

1. **Create a new environment**:
    ```bash
    conda create --name air-quality-dash python=3.9
    ```
2. **Activate the environment**:
    ```bash
    conda activate air-quality-dash
    ```
3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Option 2: Using Shell/Terminal

If you prefer using a virtual environment or pipenv, follow these steps:

1. **Create a new project directory**:
    ```bash
    mkdir proyek_analisis_data
    cd proyek_analisis_data
    ```
2. **Set up pipenv** (if not already installed):
    ```bash
    pip install pipenv
    ```
3. **Install dependencies**:
    ```bash
    pipenv install
    pipenv shell
    pip install -r requirements.txt
    ```

## Running the Streamlit App

Once the environment is set up, you can run the dashboard with:

```bash
streamlit run guanyuan_air_quality_dashboard.py
