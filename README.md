# 📊 Health Analytics Engine v1.0

A high-performance Python data pipeline and interactive web dashboard built to process, clean, and visualize large-scale cardiovascular health data.

## 🚀 Project Overview
This project demonstrates end-to-end data engineering and full-stack machine learning deployment. It ingests raw, messy health records (100,000+ patients), mathematically processes the data using vectorized operations, and serves the cleaned insights through a custom-styled, interactive local web application.

### Key Features
* **Defensive Data Engineering:** Built-in Python error handling (`try/except`) and Pandas data scrubbing (`dropna`, strict type-checking) to automatically catch and drop corrupted data (e.g., missing weights, string characters in integer columns, zero-height calculations) without crashing the pipeline.
* **Vectorized Processing:** Replaced standard loops with Pandas vectorized operations to calculate Body Mass Index (BMI) and health classifications for 100,000 rows in milliseconds.
* **Synthetic Data Generation:** Includes a custom NumPy script to generate statistically realistic, large-scale mock patient data for pipeline stress-testing.
* **Interactive UI:** A live dashboard built with Streamlit, featuring custom CSS injection to override default themes and render a high-contrast, cinematic dark mode aesthetic.
* **Data Visualization:** Integrated Matplotlib charts to display national health distribution curves dynamically based on the cleaned data output.

## 🛠️ Tech Stack
* **Backend Pipeline:** Python, Pandas, NumPy
* **Frontend Web App:** Streamlit, HTML/CSS injected styling
* **Data Visualization:** Matplotlib

## ⚙️ How to Run Locally

**1. Generate the Raw Data**
Run the synthetic data generator to create a raw CSV file of 100,000 patient records (includes intentional data corruption for pipeline testing):
```bash
python generate_data.py