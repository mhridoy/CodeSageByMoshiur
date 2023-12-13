import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title='CodeSage By Moshiur', layout='wide', page_icon=":mage:")

# Custom CSS for Styling
st.markdown("""
<style>
    /* Primary Color Variable */
    :root {
        --primary-color: #4B8BF4;
    }
    body {
        color: #fff;
        background-color: #0E1117;
    }
    h1 {
        color: var(--primary-color);
    }
    .block-container {
        padding-top: 5rem;
    }
    .schedule-table {
        width: 100%;
        margin-bottom: 2rem;
    }
    .schedule-table th {
        background-color: #222730;
        color: #fff;
    }
    .schedule-table td {
        background-color: #222730;
        color: #fff;
        border-top: 1px solid #4B8BF4;
    }
    a {
        color: var(--primary-color);
    }
    .cool-info {
        background-color: #222730;
        border-radius: 10px;
        padding: 2rem;
        margin-bottom: 2rem;
    }
    /* For responsive design */
    @media (max-width: 768px) {
        .block-container {
            padding-top: 2rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Title and Header
st.markdown("<h1 style='text-align: center;'>CodeSage By Moshiur</h1>", unsafe_allow_html=True)

# Class Schedule
st.markdown("## Class Schedule")
schedule_data = {
    'Day': ["FriSat", "SunTue", "MonThus"],
    'Times': ["10am, 11am, 2:50pm, 4:30pm, 5:50pm, 7pm, 8pm", "5:50pm, 7pm, 8pm", "5:50pm, 7pm, 8pm"]
}
schedule_df = pd.DataFrame(schedule_data)
st.table(schedule_df.style.applymap(lambda x: "background-color: #222730; color: #fff;"))

# Best Homework of the Month
st.markdown("## Best Homework This Month")
# Assuming you have a function that fetches the best homework, you can display it here
# For now, we'll just display a placeholder
st.image("https://via.placeholder.com/800x400?text=Student's+Best+Homework", caption='Homework by Student A')

# YouTube Link and Cool Information about Python for Kids
st.markdown("## Learn More About Python for Kids")
st.markdown("[Watch our Python tutorials on YouTube](https://www.youtube.com)")
st.markdown("<div class='cool-info'>Python is a great first language for kids to learn due to its simple syntax and powerful capabilities. It's used in many areas of technology, from web development to artificial intelligence, making it a valuable skill for the future.</div>", unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>© 2023 CodeSage By Moshiur. All Rights Reserved.</p>", unsafe_allow_html=True)
