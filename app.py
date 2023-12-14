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
    'background': '#F0F2F6',
    'primary': '#34568B',
    'secondary': '#FF6F61',
    'accent': '#88B04B',
    'text': '#495057',
    'button_bg': '#FFD803',   # Make sure this key exists
    'button_hover': '#CA6702',
    'footer_bg': '#7D7DA8',   # Footer background color
    'footer_text': '#EDE9F4'  # Footer text color
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
 /* Enhanced Section Styles */
    .enhanced-section {{
        background: linear-gradient(145deg, {colors['accent']}, {colors['secondary']});
        padding: 2em;
        border-radius: 15px;
        margin-bottom: 1em;
        transition: all 0.3s ease-in-out;
        box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2);
    }}

    .enhanced-section:hover {{
        transform: translateY(-10px);
        background: linear-gradient(145deg, {colors['secondary']}, {colors['accent']});
    }}

    .section-title {{
        color: {colors['primary']};
        font-size: 1.75em;
        margin-bottom: 0.5em;
    }}

    .section-content {{
        color: {colors['background']};
        font-size: 1em;
        line-height: 1.5;
    }}

    .section-outcome {{
        color: {colors['button_bg']};
        font-weight: bold;
        font-size: 1.1em;
        margin-top: 1em;
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


# New Enhanced Level Sections
st.markdown("""
<div class="enhanced-section">
    <h2 class="section-title">Level-1: Python Programming</h2>
    <p class="section-content">
        Python is a high-level, interpreted, general-purpose programming language. 
        It is currently one of the most popular programming languages in the world. 
        Our coders will learn all the necessary coding fundamentals using this high-level language.
    </p>
    <p class="section-outcome">Final Outcome: Coding Fundamentals (Basics)</p>
</div>
<div class="enhanced-section">
    <h2 class="section-title">Level-2: Website Design</h2>
    <p class="section-content">
        Web programming essentials with HTML, CSS, and Javascript. 
        Kids of different ages will become skilled in designing interactive and responsive websites.
    </p>
    <p class="section-outcome">Final Outcome: Website Design</p>
</div>
<div class="enhanced-section">
    <h2 class="section-title">Level-3: Robotics & IOT</h2>
    <p class="section-content">
        Dive into the future-tech of Internet of Things (IOT) and robotics. 
        Students will build IOT devices and robots, learning hardware and software integration.
    </p>
    <p class="section-outcome">Final Outcome: Hardware and Software Integration</p>
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
