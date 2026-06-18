import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the theme of the web page
# 1. Force a clean layout
st.set_page_config(page_title="Health Analytics Dashboard", layout="centered")


# 2. Inject a custom CSS hack to make the dashboard match your cinematic theme
st.markdown("""
    <style>
        .stApp {
            background-color: #0B132B;
            color: #FFFFFF;
        }
        h1, h2, h3 {
            color: #4EA8DE !important;
            font-family: 'Courier New', Courier, monospace;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Health Analytics Engine v1.0")
st.markdown("---")
st.markdown("This interactive dashboard displays patient BMI classifications processed by our Python data pipeline.")

# Load the clean data
# We put this in a try/except block just in case the pipeline hasn't been run yet
try:
    df = pd.read_csv('clean_patient_report.csv')
    
    # 1. Show the raw data table
    st.subheader("Cleaned Patient Records")
    st.dataframe(df, use_container_width=True)

    # 2. Create a visual chart of the categories
    st.subheader("Patient Health Distribution")
    
    # Count how many patients are in each category
    category_counts = df['Category'].value_counts()
    
    # Build a Matplotlib chart (just like your Netflix EDA project!)
    fig, ax = plt.subplots()
    category_counts.plot(kind='bar', color=['#38bdf8', '#3b82f6', '#1e40af', '#0f172a'], ax=ax)
    ax.set_ylabel("Number of Patients")
    ax.set_xticklabels(category_counts.index, rotation=0)
    
    # Display the chart on the website
    st.pyplot(fig)

except FileNotFoundError:
    st.error("⚠️ No data found. Please run pipeline.py first to generate the clean_patient_report.csv file.")