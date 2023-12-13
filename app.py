import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title='CodeSage By Moshiur', layout='wide', page_icon="🧙‍♂️")

# Custom CSS for Styling and Animations
st.markdown("""
<style>
    /* Variables */
    :root {
        --primary-color: #21a9ff;
        --secondary-color: #ff4d6d;
        --accent-color: #21ff7a;
        --dark-bg: #000000; /* Changed background color to black */
        --light-bg: #ffffff;
        --font-family: 'Poppins', sans-serif;
    }
    
    /* Global Styles */
    body {
        font-family: var(--font-family);
        background-color: var(--dark-bg); /* Ensures the background is black */
    }
    .main {
        color: var(--light-bg);
        text-align: center;
        padding: 50px;
    }
    .main h1 {
        font-size: 3.5rem;
        animation: color-change 5s infinite alternate;
    }
    
    /* Keyframes for animations */
    @keyframes color-change {
        from { color: var(--primary-color); }
        to { color: var(--accent-color); }
    }

    /* Table Styles */
    .batch-table {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .batch-table th {
        background-color: var(--secondary-color);
        color: var(--light-bg);
        padding: 15px 0;
        font-size: 1.2rem;
    }
    .batch-table td {
        padding: 15px 0;
        color: var(--primary-color);
        border-bottom: 2px solid var(--dark-bg);
        transition: background-color 0.3s ease;
    }
    .batch-table tr:last-child td {
        border-bottom: none;
    }
    .batch-table td:hover {
        background-color: var(--secondary-color);
        color: var(--light-bg);
        cursor: pointer;
        transform: scale(1.02);
        transition: transform 0.1s ease-in-out;
    }

    /* Footer Styles */
    .footer {
        margin-top: 50px;
        padding: 20px;
        color: var(--light-bg);
    }
    
    /* Dreamers Academy Mention */
    .dreamers-mention {
        margin-top: 40px;
        padding: 15px;
        border: 2px dashed var(--secondary-color);
        border-radius: 10px;
        color: var(--secondary-color);
        font-size: 1.2rem;
    }
</style>
""", unsafe_allow_html=True)

# Main Title
st.markdown('<div class="main"><h1>CodeSage By Moshiur</h1></div>', unsafe_allow_html=True)

# Schedule Template
st.markdown('## Class Schedule')

# Schedule Data
# Make sure to fill in your actual schedule data here
schedule_data = {
    'Batch Number': [f'Batch {i+1}' for i in range(13)],
    'Schedule': [
        # Replace the following strings with the actual schedule for each batch
        "Fri & Sat: 10am, 11am",  # Batch 1
        "Fri & Sat: 2:50pm, 4:30pm",  # Batch 2
        # ... Add the actual schedule for each batch here
        "Sun & Tue: 5:50pm, 7pm",  # Batch n-1
        "Mon & Thu: 5:50pm, 7pm",  # Batch n
    ] + ["TBD"] * (13 - 4)  # Replace 4 with the actual number of schedules you've defined
}

# Creating the DataFrame
schedule_df = pd.DataFrame(schedule_data)

# Displaying the DataFrame
st.table(schedule_df)

# Dreamers Academy Mention
st.markdown("""
<div class="dreamers-mention">
As a coding instructor at <a href="https://dreamersacademy.com.bd/" target="_blank" style="color: var(--secondary-color); text-decoration: none;">Dreamers Academy</a>, I specialize in teaching Python programming to kids, helping them to unlock their potential through the power of coding.
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2023 CodeSage By Moshiur. All Rights Reserved. Powered by Dreamers Academy.</div>', unsafe_allow_html=True)
