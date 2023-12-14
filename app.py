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

# Define an advanced, soothing color scheme
colors = {
    'background': '#F7F7FF',
    'primary': '#6246EA',
    'secondary': '#E45858',
    'accent': '#D1D1E9',
    'text': '#2B2C34',
    'button_bg': '#FFD803',
    'button_hover': '#FFC30B'
}

# Custom styles
st.markdown(f"""
<style>
    /* Global Styles */
    body {{
        font-family: 'Montserrat', sans-serif;
        background-color: {colors['background']};
        color: {colors['text']};
    }}
    
    h1, h2, h3, h4, h5, h6 {{
        color: {colors['primary']};
        margin: 10px 0;
        font-weight: bold;
        text-shadow: 2px 2px 4px {colors['secondary']};
    }}

    /* Enhanced Button Style */
    .stButton > button {{
        border: none;
        border-radius: 20px;
        background-color: {colors['button_bg']};
        color: {colors['background']};
        padding: 0.5rem 1.5rem;
        margin: 0.5rem 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }}
    
    /* Enhanced Table Style */
    .stDataFrame, .stTable {{
        border-radius: 0.5rem;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }}

    /* Rest of the styles remain the same */
</style>
""", unsafe_allow_html=True)


# Header
st.markdown(f'<h1>CodeSage By Moshiur</h1>', unsafe_allow_html=True)

# Load the schedule data
schedule_df = load_schedule()

# Main content area
col1, col2 = st.columns([3, 2])
with col1:
    st.markdown('## Class Schedule 📚')
    st.dataframe(schedule_df.style.set_properties(**{
        'background-color': colors['background'],
        'color': colors['text']
    }))

with col2:
    st.markdown('## Best Homework of the Month 🌟 Sababah Subah')
    st.image('best_homework.png', caption='Incredible work by our star coder!', use_column_width=True)
    st.write("Link : https://trinket.io/turtle/4ea3424527")

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
