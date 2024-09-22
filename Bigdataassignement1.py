import streamlit as st
import pandas as pd

# Load the CSV file
@st.cache_data
def load_data():
    data = pd.read_csv('GAIA Dataset.csv')
    return data

# Load data once and use cache for better performance
data = load_data()

# Set page config (like background color)
st.set_page_config(page_title="Big Data Co & Bros", layout="centered")

# Custom CSS for background color and centering the title
st.markdown(
    """
    <style>
    .main {
        background-color: #006699; /* Peacock Blue background */
    }
    .title {
        font-size: 50px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        font-weight: bold;
    }
    .dataframe-container {
        height: 400px;
        overflow-y: scroll;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the title in the center with the custom class
st.markdown('<div class="title">Big Data Co & Bros</div>', unsafe_allow_html=True)

# Display the dataframe in a scrollable container
st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
st.dataframe(data, height=400)
st.markdown('</div>', unsafe_allow_html=True)

# Add the "Get Answer" button
if st.button('Get Answer'):
    st.write("Button clicked! Process your logic here.")
