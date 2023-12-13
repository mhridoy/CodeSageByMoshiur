import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title='CodeSage By Moshiur', layout='wide', page_icon=":rocket:")

# Assuming the primary color is a shade of blue and the background is white
# with shades of gray for containers based on the image provided.
primary_color = "#1d91d0"  # Example primary color (Streamlit blue)
background_color = "#ffffff"  # White background
container_color = "#f1f3f6"  # Light gray background for containers
text_color = "#000000"  # Black text for contrast
font_family = "Arial, sans-serif"  # Arial as a fallback

# Custom CSS for Styling
st.markdown(f"""
<style>
    body {{
        font-family: {font_family};
        background-color: {background_color};
        color: {text_color};
    }}

    .st-ae {{
        color: {primary_color};
    }}

    .st-cx {{
        background-color: {container_color};
    }}

    .header {{
        text-align: center;
        color: {primary_color};
    }}

    .header h1 {{
        font-size: 3rem;
    }}

    .batch-table {{
        width: 100%;
        margin-bottom: 2rem;
    }}

    .batch-table th {{
        background-color: {primary_color};
        color: {background_color};
    }}

    .batch-table td {{
        background-color: {container_color};
        color: {text_color};
    }}

    .dreamers-mention {{
        background-color: {container_color};
        border: 2px solid {primary_color};
        border-radius: 10px;
        padding: 1rem;
        margin: 2rem 0;
        text-align: center;
    }}

    .footer {{
        text-align: center;
        padding: 1rem;
        background-color: {container_color};
        color: {text_color};
        border-top: 3px solid {primary_color};
    }}
</style>
""", unsafe_allow_html=True)

# Main Title
st.markdown('<div class="header"><h1>CodeSage By Moshiur</h1></div>', unsafe_allow_html=True)

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

# Dreamers Academy Mention
st.markdown(f"""
<div class="dreamers-mention">
    <p>🌟 I teach Python programming at <a href="https://dreamersacademy.com.bd/" target="_blank" style="color: {primary_color};">Dreamers Academy</a>. Our curriculum is crafted to kindle a lifelong passion for coding in our students.</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2023 CodeSage By Moshiur. All Rights Reserved. In collaboration with Dreamers Academy.</div>', unsafe_allow_html=True)
