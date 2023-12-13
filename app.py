import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title='CodeSage By Moshiur', layout='wide', page_icon="🚀")

# Custom CSS for Styling
st.markdown("""
<style>
    /* Global Styles */
    body {
        background-color: #000; /* Black background */
        color: #fff; /* White text */
        font-family: 'Poppins', sans-serif;
    }

    /* Header Style */
    .header {
        color: #0f9b0f; /* Neon Green */
        text-align: center;
        padding: 2rem 0;
    }
    .header h1 {
        font-size: 3rem;
        animation: pulse 2s infinite ease-in-out;
    }

    /* Keyframe Animations */
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.1); opacity: 0.7; }
    }

    /* Table Styles */
    .stTable {
        overflow-x: auto;
    }
    table {
        border-collapse: separate;
        border-spacing: 0 15px;
    }
    th {
        background-color: #17a2b8; /* Bootstrap info color */
        color: #fff;
        font-size: 1.1rem;
    }
    td {
        background-color: #2c3e50; /* Dark slate */
        color: #17a2b8; /* Matching the header color */
        font-weight: bold;
    }
    a {
        color: #f0ad4e; /* Bootstrap warning color for links */
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }

    /* Dreamers Academy Mention */
    .dreamers-mention {
        background-color: #2c3e50;
        border: 2px solid #17a2b8;
        border-radius: 10px;
        padding: 1rem;
        margin: 2rem 0;
        text-align: center;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 1rem;
        background-color: #343a40; /* Dark gray */
        color: #adb5bd; /* Light gray */
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Main Title
st.markdown('<div class="header"><h1>CodeSage By Moshiur</h1></div>', unsafe_allow_html=True)

# Class Schedule with Google Colab Links
st.markdown('## 📅 Class Schedule')

# Schedule Data with Google Colab Links (example links used here)
schedule_data = {
    'Batch Number': [f'Batch {i+1}' for i in range(13)],
    'Schedule': ["TBD" for _ in range(13)],  # Replace 'TBD' with actual schedules
    'Google Colab Link': [f'[Link to Colab](https://colab.research.google.com/batch{i+1})' for i in range(13)]
}

# DataFrame for Schedule
schedule_df = pd.DataFrame(schedule_data)
st.table(schedule_df)

# Dreamers Academy Mention
st.markdown("""
<div class="dreamers-mention">
    <p>🌟 Proudly teaching Python programming at <a href="https://dreamersacademy.com.bd/" target="_blank" style="color: #17a2b8; text-decoration: none;">Dreamers Academy</a>. Our mission is to inspire and enable the next generation of coders.</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2023 CodeSage By Moshiur. All Rights Reserved. In collaboration with Dreamers Academy.</div>', unsafe_allow_html=True)
