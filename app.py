import streamlit as st
import pandas as pd

# Function to load schedule data from the Excel file
def load_schedule():
    file_path = 'schedule.xlsx'  # Ensure this path is correct
    return pd.read_excel(file_path)

# Page configuration
st.set_page_config(
    page_title='CodeSage By Moshiur',
    layout='wide',
    page_icon='🌟'
)

# Define a cool and soothing color scheme
colors = {
    'background': '#F0F2F6',
    'primary': '#34568B',
    'secondary': '#FF6F61',
    'accent': '#88B04B',
    'text': '#2F3E46',
    'button_bg': '#FFD662',
    'button_hover': '#FFA177'
}

# Custom styles
st.markdown(f"""
<style>
    /* Global Styles */
    body {{
        font-family: 'Segoe UI', 'Arial', sans-serif;
        background-color: {colors['background']};
        color: {colors['text']};
    }}
    
    h1 {{
        color: {colors['primary']};
        font-weight: bold;
        text-align: center;
    }}

    h2 {{
        color: {colors['secondary']};
        font-weight: normal;
        text-align: left;
    }}
    
    .stButton > button {{
        border: none;
        border-radius: 20px;
        background-color: {colors['button_bg']};
        color: {colors['background']};
        padding: 0.5rem 1rem;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }}
    
    .stButton > button:hover {{
        background-color: {colors['button_hover']};
    }}
    
    .stDataFrame, .stTable {{
        border-radius: 10px;
        border: 1px solid {colors['accent']};
    }}
    
    .dataframe th {{
        background-color: {colors['primary']};
        color: {colors['background']};
    }}
    
    .dataframe td {{
        background-color: {colors['background']};
        color: {colors['text']};
    }}

    .footer {{
        background-color: {colors['primary']};
        color: {colors['background']};
        padding: 1rem;
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        font-size: 0.875rem;
    }}

    .custom-section {{
        background-color: {colors['accent']};
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }}
    
    a {{
        color: {colors['secondary']};
        text-decoration: none;
    }}
    
    a:hover {{
        color: {colors['button_hover']};
        text-decoration: underline;
    }}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1>CodeSage By Moshiur</h1>', unsafe_allow_html=True)

# Load the schedule data
schedule_df = load_schedule()

# Main content area
col1, col2 = st.columns([3, 2])
with col1:
    st.markdown('<h2>Class Schedule 📚</h2>', unsafe_allow_html=True)
    st.dataframe(schedule_df.style.set_properties(**{
        'background-color': colors['background'],
        'color': colors['text']
    }))

with col2:
    st.markdown('<h2>Best Homework of the Month 🌟 Sababah Subah</h2>', unsafe_allow_html=True)
    st.image('best_homework.png', caption='Incredible work by our star coder!', use_column_width=True)

# Dreamers Academy Mention
st.markdown(f"""
<div class="custom-section">
    <h2>Dreamers Academy Collaboration 🎓</h2>
    <p>Join us at <a href="https://dreamersacademy.com.bd/" target="_blank">Dreamers Academy</a> and start your journey with Python programming. It's a perfect place to turn curiosity into creativity!</p>
</div>
""", unsafe_allow_html=True)

# YouTube Channel Link
youtube_url = "https://youtube.com/mhridoy"  # Replace with your actual YouTube channel link
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
