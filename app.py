import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title='CodeSage By Moshiur',
    layout='wide',
    page_icon='🌈',
)

# Custom styles
st.markdown("""
<style>
    .main {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        background-color: #eff3fe;
        color: #333;
        padding: 2rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #ff6347; /* Tomato */
        text-align: center;
    }
    .schedule-table {
        background-color: #ffffff;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    .youtube-link {
        color: #ff0000; /* YouTube red */
        font-weight: bold;
        text-decoration: none;
        padding: 0.5rem 1rem;
        background-color: #fff;
        border: 2px solid #ff0000;
        border-radius: 2rem;
        display: inline-block;
        margin: 1rem 0;
    }
    .homework-section {
        background-color: #fff;
        padding: 2rem;
        margin: 1rem 0;
        border-radius: 0.5rem;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .footer {
        background-color: #333;
        color: #fff;
        padding: 1rem;
        text-align: center;
    }
    .dreamers-mention {
        background-color: #007bff; /* Bootstrap primary blue */
        color: #fff;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<div class="main"><h1>CodeSage By Moshiur</h1></div>', unsafe_allow_html=True)

# Schedule Table
st.markdown('## Class Schedule')
schedule_data = {
    'Batch Number': [f'Batch {i+1}' for i in range(13)],
    'Schedule': ['Monday & Wednesday: 4pm - 5pm' for _ in range(13)],
    'Google Colab Link': [f'[Open in Colab](https://colab.research.google.com/batch{i+1})' for i in range(13)],
}
schedule_df = pd.DataFrame(schedule_data)
st.table(schedule_df.style.set_properties(**{'background-color': '#FFFFFF', 'color': '#333'}))

# YouTube Section
youtube_url = "https://www.youtube.com/c/YourChannelName"  # Replace with your YouTube channel link
st.markdown(f'<a href="{youtube_url}" target="_blank" class="youtube-link">Visit my YouTube Channel</a>', unsafe_allow_html=True)

# Best Homework Section
st.markdown('## Best Homework of the Month')
st.image("path_to_homework_image.jpg", caption='Great job on this project!', use_column_width=True)  # Replace with the path to your image

# Dreamers Academy Mention
st.markdown("""
<div class="dreamers-mention">
    <p>I'm a proud instructor at <a href="https://dreamersacademy.com.bd/" target="_blank" style="color: #fff;">Dreamers Academy</a>, where we teach kids the joy of coding through Python!</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2023 CodeSage By Moshiur. All Rights Reserved.</div>', unsafe_allow_html=True)
