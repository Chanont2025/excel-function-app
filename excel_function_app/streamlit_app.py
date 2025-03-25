import streamlit as st
from load_data import load_default_data, load_uploaded_data
from utils import search_functions, get_unique_categories, filter_by_category
from components import render_function_card
import pandas as pd
import difflib

st.set_page_config(page_title="Excel Function Explorer", layout="wide")
st.title("📊 Excel Function Explorer")

# Sidebar CSV Upload
st.sidebar.header("📤 Upload Your CSV")
uploaded_file = st.sidebar.file_uploader("Upload CSV with required columns", type=["csv"])

df = load_uploaded_data(uploaded_file) if uploaded_file else load_default_data()

# Sidebar Category Filter
categories = get_unique_categories(df)
selected_category = st.sidebar.selectbox("📂 Browse by Category", ["All"] + categories)

# Main Search (replace st_searchbox)
all_functions = df['Function Name'].dropna().unique().tolist()
query = st.text_input("🔍 Search Excel Function")

if query:
    matched_names = difflib.get_close_matches(query, all_functions, n=10, cutoff=0.3)
    if matched_names:
        results = df[df['Function Name'].isin(matched_names)]
        for _, row in results.iterrows():
            render_function_card(row)
    else:
        st.warning("No matching Excel functions found.")
elif selected_category != "All":
    filtered_df = filter_by_category(df, selected_category)
    for _, row in filtered_df.iterrows():
        render_function_card(row)
else:
    st.info("Use the search box or choose a category to get started.")
