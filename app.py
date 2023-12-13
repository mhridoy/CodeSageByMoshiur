import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title='CodeSage By Moshiur',
    layout='wide',
    page_icon='🌟',
)

# Define colors and style settings
primary_color = "#4E33FF"  # A vibrant purple
secondary_color = "#FF3366"  # A bright pink
accent_color = "#FDCB6E"  # A sunny yellow
background_color = "#FAFAFA"  # A light grey, to keep the focus on content
content_background_color = "#FFFFFF"
text_color = "#333333"

# Custom styles
st.markdown(f"""
<style>
    /* Global Styles */
    body {{
        font-family: 'IBM Plex Sans', sans-serif;
        background-color: {background_color};
        color: {text_color};
    }}
    
    h1, h2, h3, h4, h5, h6 {{
        color: {primary_color};
    }}
    
    .block-container {{
        padding-top: 2rem;
        padding-bottom: 2rem;
    }}

    /* Custom button styles */
    .stButton > button {{
        border-radius: 30px;
        border: 2px solid {secondary_color};
        padding: 10px 24px;
        color: {secondary_color};
    }}

    /* Streamlit's DataFrame */
    .stDataFrame {{
        border-radius: 10px;
        border: 2px solid {accent_color};
    }}

    /* Hyperlink styling */
    a {{
        color: {secondary_color};
        text-decoration: none;
    }}
    
    /* Dreamers Academy Mention */
    .dreamers-mention {{
        background-color: {primary_color};
        color: {content_background_color};
        padding: 1rem;
        border-radius: 10px;
        margin: 2rem 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
    }}
    .dreamers-mention:hover {{
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.2);
    }}

    /* Footer */
    .footer {{
        text-align: center;
        padding: 1rem;
        background-color: {secondary_color};
        color: {content_background_color};
        font-size: 0.9rem;
        border-top: 3px solid {primary_color};
    }}
</style>
""", unsafe_allow_html=True)

# Main title
st.markdown(f'<h1>CodeSage By Moshiur</h1>', unsafe_allow_html=True)

# Introduction text
st.markdown("""
Welcome to CodeSage By Moshiur, where learning to code is an adventure! Dive into our vibrant classes, check out the latest homework highlights, and visit our YouTube channel for more coding fun.
""")

# Class Schedule with Google Colab Links
st.markdown('## 📅 Class Schedule')
# Schedule Data with Google Colab Links (example links used here)
schedule_data = {
    'Batch Number': [f'Batch {i+1}' for i in range(6)],
    'Schedule': ['Mon & Wed: 4pm - 5pm', 'Tue & Thu: 2pm - 3pm', 'Fri: 5pm - 6pm', 'Sat: 10am - 12pm', 'Sun: 1pm - 3pm', 'Mon & Wed: 6pm - 7pm'],
    'Google Colab Link': [f'[Open Colab](https://colab.research.google.com/batch{i+1})' for i in range(6)]
}
schedule_df = pd.DataFrame(schedule_data)
st.dataframe(schedule_df.style.set_properties(**{'background-color': content_background_color, 'color': text_color}))

# YouTube Section
youtube_url = "https://www.youtube.com/c/YourChannelName"  # Replace with your YouTube channel link
st.markdown(f'<a href="{youtube_url}" target="_blank" class="youtube-link">🎥 Visit our YouTube Channel</a>', unsafe_allow_html=True)

# Best Homework of the Month Section
st.markdown('## 🌟 Best Homework Showcase')
# Assuming you have a function to fetch the best homework image
best_homework_img = 'path_to_best_homework_image.jpg'  # Replace with the path to your best homework image
st.image(best_homework_img, caption='Incredible work by our star coder this month!', use_column_width=True)

# Dreamers Academy Mention
st.markdown(f"""
<div class="dreamers-mention">
    <h2>🎓 Dreamers Academy</h2>
    <p>At Dreamers Academy, we empower our students with the skills they need to become the next generation of problem solvers and innovators. Learn Python with us and start your coding journey today!</p>
    <a href="https://dreamersacademy.com.bd/" target="_blank">Visit Dreamers Academy</a>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown(f"""
<div class="footer">
    © 2023 CodeSage By Moshiur. All Rights Reserved.
</div>
""", unsafe_allow_html=True)
