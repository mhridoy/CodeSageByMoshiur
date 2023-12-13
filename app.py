import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title='CodeSage By Moshiur', layout='wide', page_icon="🚀")

# Custom CSS for Styling
st.markdown("""
<style>
    /* Global Styles */
    body {
        background-color: #000; /* Black background for high contrast */
        color: #fff; /* White text for readability */
        font-family: 'Poppins', sans-serif;
    }

    /* Main Header Style */
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
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.1); opacity: 0.7; }
        100% { transform: scale(1); opacity: 1; }
    }

    /* Table Styles */
    .stTable {
        overflow-x: auto;
    }
    table {
        border-collapse: separate;
        border-spacing: 0 15px; /* Space between rows */
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

    /* Dreamers Academy Mention */
    .dreamers-mention {
        background-color: #2c3e50; /* Dark slate */
        border: 2px solid #17a2b8; /* Border color */
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

# Class Schedule
st.markdown('## 📅 Class Schedule')

# Schedule Data
schedule_data = {
    'Batch Number': [f'Batch {i+1}' for i in range(13)],
    'Schedule': ["TBD" for _ in range(13)]  # Replace 'TBD' with actual schedules
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
