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
    page_icon='🌟',
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# Define a fresh and minimalistic color scheme
colors = {
    'background': '#FFFFFF',  # White background for a clean look
    'primary': '#4A4E69',     # Dark blue for elegance and contrast
    'secondary': '#9A8C98',   # Soft purple for a touch of color
    'accent': '#C9ADA7',      # Muted pink for highlights
    'text': '#22223B',        # Almost black for main text
    'footer_bg': '#4A4E69',   # Dark blue for the footer
    'footer_text': '#FFFFFF'  # White text for footer
}

# Custom styles
st.markdown(f"""
<style>
    /* Global Styles */
    body {{
        font-family: 'Segoe UI', sans-serif;
        background-color: {colors['background']};
        color: {colors['text']};
    }}

    h1 {{
        color: {colors['primary']};
        font-size: 2.5em;
        text-align: center;
    }}

    h2 {{
        color: {colors['secondary']};
        font-size: 1.75em;
    }}

    /* Custom Section Style */
    .custom-section {{
        background-color: {colors['accent']};
        padding: 2em;
        border-radius: 12px;
        margin-bottom: 1em;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }}
 /.course-section {{
        padding: 1rem;
        border-left: 5px solid {colors['accent']};
        background-color: {colors['background']};
        margin-bottom: 1rem;
    }}

    .course-title {{
        color: {colors['primary']};
        font-weight: bold;
    }}

    .course-description {{
        color: {colors['text']};
    }}
    /* Link Style */
    a {{
        color: {colors['secondary']};
        text-decoration: none;
    }}

    a:hover {{
        color: {colors['primary']};
        text-decoration: underline;
    }}
 /* Hiding Streamlit elements */
    .css-1y0tads, .css-1v3fvcr, .css-1r6o8ze {{
        visibility: hidden;
    }}
    footer {{
        visibility: hidden;
    }}
    /* Adjust the padding at the bottom of the page */
    .block-container {{
        padding-bottom: 5rem;
    }}
    /* Footer Style */
    .footer {{
        background-color: {colors['footer_bg']};
        color: {colors['footer_text']};
        padding: 1em;
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
    }}

    /* Table Style */
    .stDataFrame, .stTable {{
        border-radius: 8px;
        overflow: hidden;
    }}

    .dataframe th {{
        background-color: {colors['secondary']};
        color: {colors['text']};
    }}

    .dataframe td {{
        background-color: {colors['background']};
        color: {colors['text']};
    }}

    /* Button Style */
    .stButton > button {{
        border: 2px solid {colors['secondary']};
        border-radius: 20px;
        background-color: {colors['accent']};
        color: {colors['text']};
        padding: 0.5rem 1rem;
        transition: all 0.3s;
    }}

    .stButton > button:hover {{
        background-color: {colors['primary']};
        color: {colors['background']};
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
        'background-color': colors['background'],
        'color': colors['text']
    }))

with col2:
    st.markdown('<h2>Best Homework of the Month 🌟</h2>', unsafe_allow_html=True)
    # Replace with the actual image URL or path
    st.image('best_homework.png', caption='Incredible work by our star coder!', use_column_width=True)

# Course Sections
courses = [
    {"title": "Level-1: Python Programming", 
     "description": "Python is a high-level, interpreted, general-purpose programming language..."},
    {"title": "Level-2: Website Design", 
     "description": "Web programming essentials with HTML, CSS, and Javascript..."},
    {"title": "Level-3: Robotics & IOT", 
     "description": "Dive into the future-tech of Internet of Things (IOT) and robotics..."}
]

for course in courses:
    st.markdown(f"""
    <div class="course-section">
        <h2 class="course-title">{course['title']}</h2>
        <p class="course-description">{course['description']}</p>
    </div>
    """, unsafe_allow_html=True)

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
