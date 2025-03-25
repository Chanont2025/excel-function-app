import pandas as pd
import streamlit as st
import os

def load_default_data():
    csv_path = os.path.join(os.path.dirname(__file__), "Excel_functions_EN.csv")
    return pd.read_csv(csv_path)


def load_uploaded_data(uploaded_file):
    try:
        return pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Error loading uploaded file: {e}")
        return None
