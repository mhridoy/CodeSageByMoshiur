import streamlit as st
import pandas as pd
import sys
import io
from streamlit_ace import st_ace
# Function to load schedule data from the Excel file
def load_schedule():
    file_path = 'schedule03.xlsx'  # Ensure this path is correct
    return pd.read_excel(file_path)

# Page configuration
st.set_page_config(
    page_title='CodeSage By Moshiur',
    layout='wide',
    page_icon='🦋',
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# Enhanced color scheme
colors = {
    'background': '#F0E6F6',  # Soothing lavender background
    'primary': '#5D3FD3',     # Rich purple for primary elements
    'secondary': '#A391E6',   # Lighter purple for secondary elements
    'accent': '#D3CCE3',      # Soft lilac for accents
    'text': '#382933',        # Dark purple for text, ensuring readability
    'footer_bg': '#5D3FD3',   # Footer background
    'footer_text': '#EDE9F4'  # Footer text
}

# Custom styles with interactive elements
st.markdown(f"""
<style>
    /* Global Styles */
    /* ...existing styles... */

    /* Enhanced Button Style with Hover Effect */
    .stButton > button {{
        background-color: {colors['accent']};
        color: {colors['text']};
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 25px;
        transition: background-color 0.3s, transform 0.3s;
    }}

    .stButton > button:hover {{
        background-color: {colors['secondary']};
        transform: translateY(-2px);
    }}

    /* Enhanced Input Fields */
    .stTextInput > div > div > input {{
        border-radius: 20px;
        padding: 10px;
    }}

    /* Enhanced Tab Style */
    .stTabs > div > button {{
        border: none;
        padding: 1rem;
        border-radius: 20px;
        transition: background-color 0.3s;
    }}

    .stTabs > div > button:focus {{
        box-shadow: none;
        background-color: {colors['secondary']};
    }}

    /* Enhanced Dataframe Style */
    /* ... */
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(f'<h1> Dreamers Academy - Track 3 | CodeSage By Moshiur</h1>', unsafe_allow_html=True)

# Load the schedule data
schedule_df = load_schedule()
# Function to display class schedule
def display_schedule():
    st.markdown('<h2>Class Schedule 📚</h2>', unsafe_allow_html=True)
    st.dataframe(schedule_df.style.set_properties(**{
        'background-color': colors['background'],
        'color': colors['text']
    }))

# Function to display best homework
def display_homework():
    st.markdown('<h2>Best Homework of the Month 🌟</h2>', unsafe_allow_html=True)
    st.image('best_homework02.png', caption='Incredible work by our student!', use_column_width=True)

# Function for Python code editor
def python_editor():
    st.markdown("## Python Code Editor")
    user_code = st_ace(language='python', theme='monokai', key='code-editor')
    user_input = st.text_input("Enter input (like a command-line)", key='user-input')
    if st.button("Run Code"):
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        try:
            if user_input:
                exec(f"user_input = '{user_input}'\n{user_code}", globals())
            else:
                exec(user_code)
        except Exception as e:
            st.error(f"Error: {e}")
        finally:
            sys.stdout = old_stdout
        output = redirected_output.getvalue()
        st.text_area("Output:", value=output, height=300)

# Function for Python Turtle Graphics (assuming you have a way to embed this)
def python_turtle_graphics():
    st.markdown("## Python Turtle Graphics")

    trinket_embed_url = "https://trinket.io/embed/python/f3311da13d"
    st.components.v1.iframe(trinket_embed_url, height=1000, scrolling=False)

# Function to display courses
def display_courses():
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



# Main app layout with tabs
tab1, tab2, tab3, tab4 = st.tabs(["Schedule", "Homework", "Python Editor", "Turtle Graphics"])

with tab1:
    display_schedule()

with tab2:
    display_homework()

with tab3:
    python_editor()

with tab4:
    python_turtle_graphics()

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
    © 2024 CodeSage By Moshiur. All Rights Reserved.
</div>
""", unsafe_allow_html=True)
