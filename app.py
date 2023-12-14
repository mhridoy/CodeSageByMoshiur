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

# Define a modern and soothing color scheme
colors = {
    'background': '#F3F2F7',  # A very soft gray for a serene background
    'primary': '#7D7DA8',     # A gentle purple for a calming primary color
    'secondary': '#BFA2DB',   # A light purple for secondary elements
    'accent': '#E2D4F0',      # A very light purple for accenting elements
    'text': '#504A65',        # A darker purple for text for contrast
    'footer_bg': '#7D7DA8',   # A medium purple for the footer background
    'footer_text': '#EDE9F4'  # A light purple for footer text
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
 /* New Section Styles */
    .level-section {{
        background-color: {colors['accent']};
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }}

    .level-header {{
        color: {colors['primary']};
        font-size: 1.5em;
        margin-bottom: 10px;
    }}

    .level-content {{
        color: {colors['text']};
        line-height: 1.6;
    }}

    .final-outcome {{
        color: {colors['secondary']};
        font-weight: bold;
        margin-top: 10px;
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


# New Level Sections
st.markdown("""
<div class="level-section">
    <h2 class="level-header">Level-1: Python Programming</h2>
    <p class="level-content">
        Python is a high-level, interpreted, general-purpose programming language. 
        It is currently one of the most popular programming languages in the world. 
        Our coders will learn all the necessary coding fundamentals using this high-level language.
    </p>
    <p class="final-outcome">Final Outcome: Coding Fundamentals (Basics)</p>
</div>
<div class="level-section">
    <h2 class="level-header">Level-2: Website Design</h2>
    <p class="level-content">
        Whenever you are a web programmer, you will learn and understand the necessity of HTML and CSS. 
        Kids of different ages can work with HTML and CSS codes to become excellent web programmers. 
        They are going to get the benefit of knowing the fundamentals of HTML and CSS to design a website.
        Additionally, they will learn Javascript and a front end design framework for interactive websites.
    </p>
    <p class="final-outcome">Final Outcome: Website Design</p>
</div>
<div class="level-section">
    <h2 class="level-header">Level-3: Robotics & IOT</h2>
    <p class="level-content">
        Internet of Things (IOT) refers to objects/things that are connected and communicate via the internet. 
        In this level, they will build IOT devices and fully functional robots, learning about hardware and software integration.
    </p>
    <p class="final-outcome">Final Outcome: Hardware and Software Integration</p>
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
