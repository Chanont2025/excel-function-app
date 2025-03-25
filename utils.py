import re
import streamlit as st

def search_functions(df, query):
    return df[df['Function Name'].str.contains(query, case=False, na=False)]

def parse_tutorial_steps(tutorial):
    return tutorial.split("\n") if isinstance(tutorial, str) else []

def get_unique_categories(df):
    return sorted(df['Category'].dropna().unique())

def filter_by_category(df, category):
    return df[df['Category'] == category]
