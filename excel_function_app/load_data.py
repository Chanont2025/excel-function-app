import streamlit as st
import pandas as pd
import gdown
import os

CSV_PATH = "excel_function_app/Excel_functions_EN.csv"

@st.cache_data
def download_from_gdrive():
    if not os.path.exists(CSV_PATH):
        file_id = st.secrets["remote_file"]["gdrive_file_id"]
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, CSV_PATH, quiet=False)
    return pd.read_csv(CSV_PATH)

def load_default_data():
    try:
        return download_from_gdrive()
    except Exception as e:
        st.error(f"❌ Failed to load data: {e}")
        return pd.DataFrame()
