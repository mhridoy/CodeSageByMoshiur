import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title='CodeSage By Moshiur', layout='wide', page_icon="🧙‍♂️")

# Custom CSS for Styling
st.markdown("""
<style>
    /* Primary Color Variable */
    :root {
        --primary-color: #0eaff7;
        --secondary-color: #ff4d6d;
        --accent-color: #20c997;
        --background-color: #0e1117;
        --font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    body {
        color: #fff;
        background-color: var(--background-color);
        font-family: var(--font-family);
    }
    h1, h2, h3 {
        color: var(--primary-color);
        text-align: center;
    }
    .big-title {
        font-size: 4rem;
        font-weight: 700;
        margin: 1rem 0;
    }
    .schedule-table {
        width: 100%;
        margin-bottom: 2rem;
        box-shadow: 0 2px 12px 0 rgba(0,0,0,0.2);
    }
    .schedule-table th {
        background-color: var(--primary-color);
        color: #fff;
        padding: 1rem;
    }
    .schedule-table td {
        background-color: var(--background-color);
        color: #fff;
        border-top: 2px solid var(--secondary-color);
        padding: 1rem;
    }
    .schedule-table td:hover {
        background-color: var(--accent-color);
        cursor: pointer;
        color: var(--background-color);
        transform: scale(1.02);
        transition: transform 0.1s ease-in-out;
    }
    a {
        color: var(--primary-color);
        text-decoration: none;
        font-weight: bold;
    }
    a:hover {
        color: var(--secondary-color);
    }
    .cool-info {
        background-color: var(--secondary-color);
        border-radius: 10px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 14px 0 rgba(0,0,0,0.3);
    }
    .footer {
        text-align: center;
        padding: 1rem;
        color: var(--secondary-color);
    }
</style>
""", unsafe_allow_html=True)

# Title and Header
st.markdown("<h1 class='big-title'>CodeSage By Moshiur</h1>", unsafe_allow_html=True)

# Class Schedule
st.markdown("## Class Schedule")
schedule_data = {
    'Day': ["FriSat", "SunTue", "MonThus"],
    'Times': ["10am, 11am, 2:50pm, 4:30pm, 5:50pm, 7pm, 8pm", "5:50pm, 7pm, 8pm", "5:50pm, 7pm, 8pm"]
}
schedule_df = pd.DataFrame(schedule_data)
st.table(schedule_df.style.set_table_styles([
        {'selector': 'th', 'props': [('background-color', 'var(--primary-color)'), ('color', 'white')]},
        {'selector': 'td:hover', 'props': [('background-color', 'var(--accent-color)'), ('color', 'var(--background-color)'), ('transform', 'scale(1.02)'), ('transition', 'transform 0.1s ease-in-out')]},
        {'selector': 'td', 'props': [('background-color', 'var(--background-color)'), ('color', 'white'), ('border-top', '2px solid var(--secondary-color)')]},
    ]))

# Best Homework of the Month
st.markdown("## Best Homework This Month")
# Assuming you have a function that fetches the best homework, you can display it here
# For now, we'll just display a placeholder
st.image("https://via.placeholder.com/800x400?text=Student's+Best+Homework", caption='Homework by Student A')

# YouTube Link and Cool Information about Python for Kids
st.markdown("## Learn More About Python for Kids")
st.markdown("[Check out our Python tutorials on YouTube](https://www.youtube.com)", unsafe_allow_html=True)
st.markdown("<div class='cool-info'>Python is an excellent language for kids to
