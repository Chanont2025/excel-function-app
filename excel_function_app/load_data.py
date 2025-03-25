import pandas as pd
import streamlit as st

def load_default_data():
    return pd.read_csv("Excel_functions_EN.csv")

def load_uploaded_data(uploaded_file):
    try:
        return pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Error loading uploaded file: {e}")
        return None
