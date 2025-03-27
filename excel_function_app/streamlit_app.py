import streamlit as st
from load_data import load_default_data, load_uploaded_data
from utils import search_functions, get_unique_categories, filter_by_category
from components import render_function_card
import pandas as pd
from st_searchbox import st_searchbox

st.set_page_config(page_title="Excel Function Explorer", layout="wide")
st.title("📊 Excel Function Explorer")

# Sidebar CSV Upload
st.sidebar.header("📤 Upload Your CSV")
uploaded_file = st.sidebar.file_uploader("Upload CSV with required columns", type=["csv"])

df = load_uploaded_data(uploaded_file) if uploaded_file else load_default_data()

# Sidebar Category Filter
categories = get_unique_categories(df)
selected_category = st.sidebar.selectbox("📂 Browse by Category", ["All"] + categories)

# Main Search
query = st_searchbox(lambda x: df[df['Function Name'].str.contains(x, case=False)]['Function Name'].tolist(),
                     key="searchbox",
                     label="🔍 Search Excel Functions")

if query:
    results = search_functions(df, query)
    for _, row in results.iterrows():
        render_function_card(row)

elif selected_category != "All":
    filtered_df = filter_by_category(df, selected_category)
    for _, row in filtered_df.iterrows():
        render_function_card(row)
else:
    st.info("Use the search box or choose a category to get started.")
