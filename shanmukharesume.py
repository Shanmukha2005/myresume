import streamlit as st
from streamlit.components.v1 import html
# Open and read the HTML file
with open("shanmukharesume.html", "r", encoding="utf-8") as f:
    html_content = f.read()





import streamlit as st

# Configure page settings
st.set_page_config(
    page_title="Full Height App",
    layout="wide",
    initial_sidebar_state="auto"
)

# Custom CSS for full height
st.markdown("""
    <style>
    /* Full viewport height */
    .main > div {
        min-height: 100vh;
        padding: 1rem 2rem !important;
    }

    /* Remove default Streamlit spacing */
    .stApp {
        margin: 0 !important;
        padding: 0 !important;
        max-width: none !important;
    }

    /* Full-height containers */
    .full-height {
        height: calc(100vh - 100px) !important;  /* Adjust for header/footer */
        overflow-y: auto;
    }
    
    /* Fix iframe height */
    .st-emotion-cache-1v0mbdj {
        height: 100vh !important;
    }
    </style>
    """, unsafe_allow_html=True)







# Render the HTML/JS website
st.title("")
html(html_content, height=2000)
