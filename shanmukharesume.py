import streamlit as st
from streamlit.components.v1 import html
# Open and read the HTML file
with open("shanmukharesume.html", "r", encoding="utf-8") as f:
    html_content = f.read()


import streamlit as st

# Set fixed dimensions and disable mobile view
st.markdown("""
    <style>
    /* Force desktop layout */
    .main > div {
        min-width: 1024px !important;
        max-width: 1366px !important;  /* Typical laptop screen width */
        margin: 0 auto;
        padding: 2rem;
    }

    /* Hide mobile overflow */
    .reportview-container .main {
        overflow: hidden;
    }

    /* Mobile device warning */
    @media (max-width: 1023px) {
        .desktop-content {
            display: none !important;
        }
        .mobile-warning {
            display: block !important;
            padding: 2rem;
            text-align: center;
            color: red;
            font-size: 24px;
        }
    }

    @media (min-width: 1024px) {
        .mobile-warning {
            display: none !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Add mobile warning message
st.markdown("""
    <div class="mobile-warning">
        ⚠️ This application is only available on laptop/desktop devices!
    </div>
    """, unsafe_allow_html=True)

# Main content (only visible on laptops/desktops)
st.markdown('<div class="desktop-content">', unsafe_allow_html=True)

# Your laptop-only content
st.set_page_config(layout="wide")
st.title("Laptop-Only Application")
st.header("This app is optimized for laptop/desktop viewing")

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Control Panel")
        slider_value = st.slider("Select value", 0, 100, 50)
        
    with col2:
        st.subheader("Visualization")
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
        st.line_chart(chart_data, height=400)

st.markdown('</div>', unsafe_allow_html=True)

# Block mobile zooming
st.markdown("""
    <meta name="viewport" content="width=1024, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, minimum-scale=1.0">
    """, unsafe_allow_html=True)


# Render the HTML/JS website
st.title("")
html(html_content, height=2000)
