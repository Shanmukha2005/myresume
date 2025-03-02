import streamlit as st
from streamlit.components.v1 import html

import streamlit as st
import pandas as pd
import numpy as np

# Configure page
st.set_page_config(
    page_title="Responsive App",
    layout="wide",
    initial_sidebar_state="auto"
)

# Responsive CSS
st.markdown("""
    <style>
    @media (max-width: 768px) {
        /* Mobile styles */
        .main > div {
            padding: 0.5rem !important;
        }
        .stChart {
            height: 300px !important;
        }
    }
    
    @media (min-width: 769px) {
        /* Desktop styles */
        .main > div {
            padding: 2rem !important;
            max-width: 1200px;
            margin: 0 auto;
        }
        .stChart {
            height: 500px !important;
        }
    }
    
    /* Always show vertical scroll */
    .main {
        overflow-y: auto;
    }
    </style>
    """, unsafe_allow_html=True)

# App content
col1, col2 = st.columns([1, 2])
with col1:
    st.header("Controls")
    slider_val = st.slider("Select value", 0, 100)

with col2:
    st.header("Visualization")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

# Open and read the HTML file
with open("shanmukharesume.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render the HTML/JS website
st.title("")
html(html_content, height=2000)
