import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title='CodeSage By Moshiur', layout='wide', page_icon="🌟")

# Define a modern color scheme
colors = {
    "primary": "#0083B8",
    "secondary": "#00B4D8",
    "accent": "#90E0EF",
    "background": "#CAF0F8",
    "text": "#0077B6",
    "dark_text": "#03045E",
    "light_text": "#ffffff"
}

# Custom styles
st.markdown(f"""
<style>
    /* Global Styles */
    body {{
        font-family: 'Roboto', sans-serif;
        background-color: {colors['background']};
        color: {colors['text']};
    }}
    
    h1, h2, h3 {{
        color: {colors['primary']};
    }}
    
    .stButton > button {{
        border-radius: 30px;
        border: none;
        background-color: {colors['accent']};
        color: {colors['dark_text']};
        padding: 10px 24px;
        margin: 0px 10px;
        transition: background-color 0.3s ease;
    }}
    
    .stButton > button:hover {{
        background-color: {colors['secondary']};
    }}
    
    .stDataFrame {{
        border-radius: 10px;
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.15);
    }}
    
    .dataframe {{
        width: 100%;
        border-collapse: collapse;
    }}
    
    .dataframe th {{
        background-color: {colors['primary']};
        color: {colors['light_text']};
    }}
    
    .dataframe td, .dataframe th {{
        padding: 10px;
        border: 1px solid {colors['accent']};
        text-align: left;
    }}
    
    .footer {{
        background-color: {colors['secondary']};
        color: {colors['light_text']};
        padding: 10px;
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
    }}
    
    .youtube-section {{
        background-color: {colors['primary']};
        color: {colors['light_text']};
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        text-align: center;
        transition: transform 0.3s ease;
    }}
    
    .youtube-section:hover {{
        transform: scale(1.05);
    }}

    .homework-section {{
        background-color: {colors['accent']};
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        text-align: center;
        transition: transform 0.3s ease;
    }}
    
    .homework-section:hover {{
        transform: scale(1.05);
    }}
    
    a {{
        color: {colors['dark_text']};
        text-decoration: none;
    }}
    
    a:hover {{
        color: {colors['secondary']};
        text-decoration: underline;
    }}
    
</style>
""", unsafe_allow_html=True)

# Header with Title and Subtitle
st.markdown(f'<h1>CodeSage By Moshiur</h1>', unsafe_allow_html=True)

# YouTube Link Section
youtube_url = "https://www.youtube.com/c/YourChannelName"  # Replace with your YouTube channel link
st.markdown(f"""
<div class="youtube-section">
    <h2>Explore Our YouTube Channel</h2>
    <a href="{youtube_url}" target="_blank" class="youtube-link">Visit YouTube</a>
</div>
""", unsafe_allow_html=True)

# Class Schedule Section
st.markdown('## Class Schedule')
schedule_data = {
    'Batch Number': [f'Batch {i+1}' for i in range(6)],
    'Schedule': ['Monday & Wednesday: 4pm - 5pm', 'Tuesday & Thursday: 2pm - 3pm', 'Friday: 5pm - 6pm', 'Saturday: 10am - 12pm', 'Sunday: 1pm - 3pm', 'Monday & Wednesday: 6pm - 7pm'],
    'Google Colab Link': [f'[Open Colab](https://colab.research.google.com/batch{i+1})' for i in range(6)]
}
schedule_df = pd.DataFrame(schedule_data)
st.dataframe(schedule_df.style.set_properties(**{'background-color': colors['background'], 'color': colors['text']}))

# Homework Showcase Section
st.markdown("""
<div class="homework-section">
    <h2>Best Homework of the Month</h2>
    <p>Check out this month's star project!</p>
    <!-- Replace 'path_to_homework_image.jpg' with the actual path to your best homework image -->
    <img src="path_to_homework_image.jpg" alt="Best Homework" style="max-width: 100%; border-radius: 10px;">
</div>
""", unsafe_allow_html=True)

# Dreamers Academy Mention
st.markdown(f"""
<div class="youtube-section">
    <h2>Dreamers Academy</h2>
    <p>As a proud instructor at <a href="https://dreamersacademy.com.bd/" target="_blank">Dreamers Academy</a>, I'm excited to teach Python programming to our brilliant students.</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown(f"""
<div class="footer">
    © 2023 CodeSage By Moshiur. All Rights Reserved.
</div>
""", unsafe_allow_html=True)
