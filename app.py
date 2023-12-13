import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title='CodeSage By Moshiur', layout='wide')

# Custom CSS for Styling
st.markdown("""
<style>
    body {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    .main-title {
        color: #4B8BF4;
        text-align: center;
        margin-bottom: 50px;
    }
    .batch-table {
        margin: auto;
        border-collapse: collapse;
        width: 90%;
        font-size: 18px;
    }
    .batch-table td, .batch-table th {
        border: 1px solid #ddd;
        padding: 12px;
        text-align: center;
    }
    .batch-table tr {
        transition: background-color 0.3s ease;
    }
    .batch-table tr:nth-child(even) {
        background-color: #f8f9fa;
    }
    .batch-table tr:hover {
        background-color: #e9ecef;
    }
    .batch-table th {
        background-color: #6c757d;
        color: white;
    }
    .colab-link {
        color: #28a745;
        text-decoration: none;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='main-title'>CodeSage By Moshiur</h1>", unsafe_allow_html=True)

# Data for the Table
data = {
    'Batch': [f'Batch {i+1}' for i in range(13)],
    'Google Colab Link': [f'<a href="http://colab.link/batch{i+1}" class="colab-link" target="_blank">Open Link</a>' for i in range(13)]
}
df = pd.DataFrame(data)

# Display the Table with Enhanced Styling
st.markdown(df.to_html(classes='batch-table', escape=False, index=False), unsafe_allow_html=True)

# Footer or Additional Information
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>© 2023 CodeSage By Moshiur. All Rights Reserved.</p>", unsafe_allow_html=True)
