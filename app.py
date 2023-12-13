import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title='CodeSage By Moshiur', layout='wide', page_icon="🚀")

# Custom CSS for Styling
st.markdown("""
<style>
    /* Global Styles */
    body {
        font-family: 'Roboto', sans-serif;
        background-color: #0E0E10; /* Almost black for a sleek look */
        color: #E8E6E3; /* Soft white for text */
    }

    /* Header Style */
    .header {
        color: #21A1F1; /* Bright blue for a techy feel */
        text-align: center;
        padding: 2rem 0;
    }
    .header h1 {
        font-size: 4rem;
        font-weight: 700;
        margin: 0;
    }
    .header h1 span {
        display: block;
        font-size: 2rem;
        margin-top: 0.5rem;
    }

    /* Table Styles */
    .stTable {
        box-shadow: 0px 2px 4px rgba(0,0,0,0.1);
    }
    .stTable table {
        border-spacing: 0 15px; /* Space between rows */
    }
    .stTable th {
        background-color: #21A1F1; /* Bright blue header */
        color: #FFFFFF;
        font-size: 1.1rem;
    }
    .stTable td {
        background-color: #1C1C1E; /* Darker background for rows */
        color: #21A1F1; /* Bright blue text for contrast */
        font-weight: bold;
    }

    /* YouTube Link Style */
    .youtube-link {
        color: #FF0000; /* Bright red for YouTube branding */
        font-size: 1.5rem;
        font-weight: bold;
        text-align: center;
        padding: 1rem 0;
    }

    /* Homework Showcase */
    .homework-section {
        background-color: #1C1C1E; /* Dark background for emphasis */
        padding: 2rem;
        border-radius: 10px;
        margin-top: 2rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .homework-section h2 {
        color: #21A1F1; /* Bright blue */
        font-size: 2rem;
    }

    /* Dreamers Academy Mention */
    .dreamers-mention {
        background-color: #1C1C1E; /* Darker slate */
        color: #21A1F1; /* Bright blue text */
        padding: 1rem;
        margin: 2rem 0;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 1rem;
        background-color: #111113; /* Slightly lighter black */
        color: #E8E6E3; /* Soft white */
        font-size: 0.9rem;
        margin-top: 5rem;
    }
</style>
""", unsafe_allow_html=True)

# Header with Title and Subtitle
st.markdown("""
<div class="header">
    <h1>CodeSage By Moshiur <span>Empowering the Next Generation of Coders</span></h1>
</div>
""", unsafe_allow_html=True)

# YouTube Link Section
youtube_url = "https://www.youtube.com/c/YourChannel"  # Replace with your YouTube channel link
st.markdown(f"""
<p class="youtube-link">
    Check out my <a href="{youtube_url}" target="_blank">YouTube channel</a> for more tutorials!
</p>
""", unsafe_allow_html=True)

# Class Schedule with Google Colab Links
st.markdown('## 📅 Class Schedule')

# Schedule Data with Google Colab Links (example links used here)
schedule_data = {
    'Batch Number': [f'Batch {i+1}' for i in range(13)],
    'Schedule': ["TBD" for _ in range(13)],  # Replace 'TBD' with actual schedules
    'Google Colab Link': [f'[Open Colab](https://colab.research.google.com/batch{i+1})' for i in range(13)]
}

# DataFrame for Schedule
schedule_df = pd.DataFrame(schedule_data)
st.table(schedule_df)

# Best Homework of the Month Section
st.markdown("""
<div class="homework-section">
    <h2>🌟 Best Homework of the Month 🌟</h2>
    <!-- Replace 'path_to_homework_image' with the actual path to the homework image -->
    <img src="path_to_homework_image" alt="Best Homework" style="width:100%; border-radius:10px;">
</div>
""", unsafe_allow_html=True)

# Dreamers Academy Mention
st.markdown("""
<div class="dreamers-mention">
    Proudly teaching Python at <a href="https://dreamersacademy.com.bd/" target="_blank">Dreamers Academy</a>, where we nurture young minds in the world of programming.
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    © 2023 CodeSage By Moshiur. All Rights Reserved. In collaboration with Dreamers Academy.
</div>
""", unsafe_allow_html=True)
