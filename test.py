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

# Import Google Font and enhanced CSS styling
st.markdown(f"""
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
<style>
    /* Apply Google Font */
    body {{
        font-family: 'Roboto', sans-serif;
        background-color: {colors['background']};
        color: {colors['text']};
    }}

    h1, h2, h3, h4, h5, h6 {{
        font-family: 'Roboto', sans-serif;
    }}

    /* Button Style with Hover Effect */
    .stButton > button {{
        background: linear-gradient(45deg, {colors['primary']}, {colors['secondary']});
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 30px;
        transition: transform 0.2s, box-shadow 0.2s;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 1rem;
    }}

    .stButton > button:hover {{
        transform: scale(1.05);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }}

    /* Custom Section Style */
    .custom-section {{
        background-color: {colors['accent']};
        padding: 2em;
        border-radius: 15px;
        margin-bottom: 1em;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }}

    .custom-section:hover {{
        transform: scale(1.03);
    }}

    /* Other Custom Styles... */
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

st.markdown(f"""
<div class="footer">
    <p>Connect with us:</p>
    <!-- Social media icons -->
    <a href="https://facebook.com/codesagebymoshiur" target="_blank"><img src="https://icons8.com/icon/118468/facebook" alt="Facebook"></a>
    <a href="https://twitter.com/" target="_blank"><img src="https://icons8.com/icon/437/twitter" alt="Twitter"></a>
    <a href="https://instagram.com/" target="_blank"><img src="https://icons8.com/icon/32292/instagram" alt="Instagram"></a>
    <p>© 2024 CodeSage By Moshiur. All Rights Reserved.</p>
</div>
""", unsafe_allow_html=True)
