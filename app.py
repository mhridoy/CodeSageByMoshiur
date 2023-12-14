import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title='CodeSage By Moshiur',
    layout='wide',
    page_icon='🌟'
)

# Define a harmonious color palette
colors = {
    'background': '#FAFAFA',  # A gentle off-white background
    'primary': '#005f73',     # A calming dark teal
    'secondary': '#0a9396',   # A soothing teal
    'accent': '#94d2bd',      # A soft green accent
    'text': '#495057',        # A dark gray for text for readability
    'button': '#ee9b00',      # A warm amber for buttons and highlights
    'button_hover': '#ca6702',  # A darker shade for button hover state
}

# Custom styles
st.markdown(f"""
<style>
    /* Global Styles */
    body {{
        font-family: 'Calibri', sans-serif;
        background-color: {colors['background']};
        color: {colors['text']};
    }}
    
    h1 {{
        color: {colors['primary']};
        font-weight: bold;
    }}
    
    h2 {{
        color: {colors['secondary']};
    }}
    
    .stButton > button {{
        border: 2px solid transparent;
        border-radius: 30px;
        background-color: {colors['button']};
        color: {colors['background']};
        padding: 0.5rem 1rem;
        transition: background-color 0.3s, border-color 0.3s;
    }}
    
    .stButton > button:hover {{
        background-color: {colors['background']};
        border-color: {colors['button_hover']};
        color: {colors['button']};
    }}
    
    .stDataFrame, .stTable {{
        border-radius: 0.5rem;
    }}
    
    .dataframe {{
        border: 2px solid {colors['accent']};
    }}
    
    .dataframe th {{
        background-color: {colors['primary']};
        color: {colors['background']};
    }}
    
    .dataframe td {{
        background-color: {colors['secondary']};
        color: {colors['background']};
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
        border-radius: 0.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }}
    
    a {{
        color: {colors['button']};
        text-decoration: none;
        transition: color 0.2s;
    }}
    
    a:hover {{
        color: {colors['button_hover']};
        text-decoration: underline;
    }}
    
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(f'<h1>CodeSage By Moshiur</h1>', unsafe_allow_html=True)

# Main content area
col1, col2 = st.columns(2)
with col1:
    st.markdown('## Class Schedule')
    # Schedule Data
    schedule_data = {
        'Batch': [f'Batch {i+1}' for i in range(6)],
        'Schedule': ['Monday & Wednesday: 4pm - 5pm' for _ in range(6)],
        'Google Colab Link': [f'[Open in Colab](https://colab.research.google.com/batch{i+1})' for i in range(6)]
    }
    # DataFrame for Schedule
    schedule_df = pd.DataFrame(schedule_data)
    st.dataframe(schedule_df)

with col2:
    st.markdown('## Best Homework of the Month')
    st.image('path_to_homework_image.jpg', caption='Incredible work by our star coder!', use_column_width=True)

# Dreamers Academy Mention
st.markdown(f"""
<div class="custom-section">
    <h2>Dreamers Academy Collaboration</h2>
    <p>As an instructor at <a href="https://dreamersacademy.com.bd/" target="_blank">Dreamers Academy</a>, I take pride in guiding students through their Python programming journey. Join us to explore the world of coding!</p>
</div>
""", unsafe_allow_html=True)

# YouTube Channel Link
st.markdown(f"""
<div class="custom-section">
    <h2>Visit our YouTube Channel</h2>
    <p>Discover more learning resources and tutorials on our <a href="https://www.youtube.com/c/YourChannelName" target="_blank">YouTube channel</a>.</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    &copy; 2023 CodeSage By Moshiur. All Rights Reserved.
</div>
""", unsafe_allow_html=True)
