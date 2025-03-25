import pandas as pd
import streamlit as st
import os
import gdown

CSV_PATH = os.path.join(os.path.dirname(__file__), "Excel_functions_EN.csv")

@st.cache_data
def download_default_csv():
    if not os.path.exists(CSV_PATH):
        try:
            file_id = st.secrets["remote_file"]["gdrive_file_id"]
            url = f"https://drive.google.com/uc?id={file_id}"
            gdown.download(url, CSV_PATH, quiet=False)
        except Exception as e:
            st.error(f"❌ Failed to download default CSV: {e}")
            return pd.DataFrame()
    return pd.read_csv(CSV_PATH)

def load_default_data():
    return download_default_csv()

def load_uploaded_data(uploaded_file):
    try:
        return pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Error loading uploaded file: {e}")
        return None
