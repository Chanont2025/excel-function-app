import streamlit as st
import pyperclip
from utils import parse_tutorial_steps

def render_function_card(row):
    st.subheader(row['Function Name'])
    st.markdown(f"**Category**: {row['Category']}")
    st.code(row['Syntax'], language='text')
    st.markdown(f"**Example**: `{row['Example']}`")
    st.markdown(f"**Description**: {row['Description']}")

    if st.button(f"Copy Syntax - {row['Function Name']}"):
        pyperclip.copy(row['Syntax'])
        st.success("Copied to clipboard!")

    st.markdown("---")
    st.markdown("### Tutorial")
    for i, step in enumerate(parse_tutorial_steps(row['Tutorial']), 1):
        st.markdown(f"**Step {i}:** {step}")
