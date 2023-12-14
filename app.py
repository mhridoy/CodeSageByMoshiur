import streamlit as st
import pandas as pd

# Function to load schedule data from the Excel file
def load_schedule():
    file_path = 'schedule.xlsx'  # Make sure this path is correct
    return pd.read_excel(file_path)

# Page configuration
st.set_page_config(
    page_title='CodeSage By Moshiur',
    layout='wide',
    page_icon='🌟'
)

# Define a modern and soothing color scheme
colors = {
    'background': '#F0F2F6',  # A soft gray for a light and airy feel
    'primary': '#34568B',     # A deep blue for a calming effect
    'secondary': '#FF6F61',   # A warm coral for a pop of energy
    'accent': '#88B04B',      # A fresh green for vibrancy
    'text': '#495867',        # A dark slate for readability
}

# Custom styles
st.markdown(f"""
<style>
    /* Global Styles */
    body {{
        font-family: 'Arial', sans-serif;
        background-color: {colors['background']};
        color: {colors['text']};
    }}
    
    h1 {{
        color: {colors['primary']};
        font-size: 2.5em;
        text-align: center;
        margin-top: 0.5em;
        margin-bottom: 0.5em;
    }}

    h2 {{
        color: {colors['secondary']};
        font-size: 1.75em;
        margin-top: 0.5em;
        margin-bottom: 0.5em;
    }}
    
    .stButton > button {{
        border: 2px solid {colors['primary']};
        border-radius: 5px;
        background-color: {colors['background']};
        color: {colors['primary']};
        padding: 0.5rem 1rem;
        transition: all 0.3s;
    }}
    
    .stButton > button:hover {{
        background-color: {colors['primary']};
        color: {colors['background']};
        border-color: {colors['secondary']};
    }}
    
    .stDataFrame, .stTable {{
        border-radius: 8px;
        overflow: hidden;
    }}

    .dataframe {{
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }}

    .dataframe th {{
        background-color: {colors['primary']};
        color: {colors['background']};
    }}

    .dataframe td {{
        background-color: {colors['accent']};
        color: {colors['text']};
    }}

    .footer {{
        background-color: {colors['primary']};
        color: {colors['background']};
        padding: 1em;
        text-align: center;
        position: fixed;
        bottom: 0;
        width: 100%;
    }}

    .custom-section {{
        background-color: {colors['background']};
        padding: 2em;
        border-radius: 10px;
        margin-top: 1em;
        margin-bottom: 1em;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }}

    a {{
        color: {colors['secondary']};
        font-weight: bold;
        text-decoration: none;
    }}

    a:hover {{
        color: {colors['primary']};
        text-decoration: underline;
    }}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(f'<h1>CodeSage By Moshiur</h1>', unsafe_allow_html=True)

# Load the schedule data
schedule_df = load_schedule()

# Main content area
col1, col2 = st.columns([3, 2])
with col1:
    st.markdown('<h2>Class Schedule 📚</h2>', unsafe_allow_html=True)
    st.dataframe(schedule_df.style.set_properties(**{
        'background-color': colors['accent'],
        'color': colors['text']
    }))

with col2:
    st.markdown('<h2>Best Homework of the Month 🌟</h2>', unsafe_allow_html=True)
    # Replace with the actual image URL or path
    st.image('best_homework.png', caption='Incredible work by our star coder!', use_column_width=True)

# Dreamers Academy Mention
st.markdown(f"""
<div class="custom-section">
    <h2>Dreamers Academy Collaboration 🎓</h2>
    <p>Join us at <a href="https://dreamersacademy.com.bd/" target="_blank">Dreamers Academy</a> and start your journey with Python programming. It's a perfect place to turn curiosity into creativity!</p>
</div>
""", unsafe_allow_html=True)

# YouTube Channel Link
youtube_url = "https://youtube.com/mhridoy"
st.markdown(f"""
<div class="custom-section">
    <h2>Explore our YouTube Channel 🎥</h2>
    <p>Check out our <a href="{youtube_url}" target="_blank">YouTube channel</a> for engaging tutorials and learning resources.</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown(f"""
<div class="footer">
    © 2023 CodeSage By Moshiur. All Rights Reserved.
</div>
""", unsafe_allow_html=True)
