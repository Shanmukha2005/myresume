import streamlit as st
from streamlit.components.v1 import html
# Open and read the HTML file
with open("shanmukharesume.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.title("")
html(html_content, height=2100)
