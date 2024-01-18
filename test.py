import streamlit as st
import pandas as pd
import sys
import io
from streamlit_ace import st_ace
# Function to load schedule data from the Excel file
def load_schedule():
    file_path = 'schedule.xlsx'  # Ensure this path is correct
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

# Define a creative and soothing light purple color scheme
colors = {
    'background': '#FAF4FF',  # A very light purple for a serene background
    'primary': '#7B2CBF',     # A deep purple for contrast
    'secondary': '#9D4EDD',   # A softer purple for secondary elements
    'accent': '#CDB4DB',      # A gentle lavender for highlights
    'text': '#4A2040',        # A darker purple for text
    'footer_bg': '#7B2CBF',   # Deep purple for the footer
    'footer_text': '#EDE9F4'  # Light purple text for the footer
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
        border-radius: 15px;
        margin-bottom: 1em;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }}

    .custom-section:hover {{
        transform: scale(1.03);
    }}

    /* Course Section Style */
    .course-section {{
        border-left: 5px solid {colors['secondary']};
        background-color: {colors['background']};
        padding: 1em;
        margin-bottom: 1em;
    }}

    .course-title {{
        color: {colors['primary']};
        font-weight: bold;
    }}

    .course-description {{
        color: {colors['text']};
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
    .stTextInput > div > div > input {{
        font-size: 20px;
    }}

    /* Hiding Streamlit elements */
    .css-1y0tads, .css-1v3fvcr, .css-1r6o8ze {{
        visibility: hidden;
    }}
    footer {{
        visibility: hidden;
    }}
    .block-container {{
        padding-bottom: 5rem;
    }}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(f'<h1> Dreamers Academy - Track 3 | CodeSage By Moshiur</h1>', unsafe_allow_html=True)

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
    st.markdown('<h2>Best Homework of the Month 🌟 Afsara </h2>', unsafe_allow_html=True)
    # Replace with the actual image URL or path
    st.image('best_homework02.png', caption='Incredible work by our star coder!', use_column_width=True)
    st.write("Code Link : https://trinket.io/python/ef2a270c85")

# Course Sections
courses = [
    {"title": "Level-1: Python Programming", 
     "description": "Python is a high-level, interpreted, general-purpose programming language..."},
    {"title": "Level-2: Website Design", 
     "description": "Web programming essentials with HTML, CSS, and Javascript..."},
    {"title": "Level-3: Robotics & IOT", 
     "description": "Dive into the future-tech of Internet of Things (IOT) and robotics..."}
]

# Selection for Python editor or Turtle graphics
activity = st.selectbox("Wanna Try Some Code: 🤗🤗", ["Python Editor", "Python Turtle Graphics"])

if activity == "Python Editor":
    # Python Code Editor Section
    st.markdown("## Python Code Editor")
    user_code = st_ace(language='python', theme='monokai', key='code-editor', height=250)
    
    # Custom styles for the Python editor
    st.markdown("""
    <style>
        .ace_editor {
            border: 2px solid #your_secondary_color;
            border-radius: 10px;
            background-color: #your_accent_color;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # User Input Section
    st.markdown("## User Input")
    user_input = st.text_area("Enter input (like a command-line)", key='user-input', height=150)
    
    # Button to run the code
    if st.button("Run Code"):
        # Check if the code is empty or contains only whitespace
        if not user_code.strip():
            st.warning('Please enter some code to run.')
        else:
            # Display a spinner and a message indicating that the code is running
            with st.spinner('Running...'):
                # Capture the standard output and handle exceptions
                old_stdout = sys.stdout
                redirected_output = sys.stdout = io.StringIO()
                
                try:
                    # Define a variable `user_input` in the local scope for the exec
                    local_vars = {"user_input": user_input}
                    # Execute the user's code
                    exec(user_code, globals(), local_vars)
                except Exception as e:
                    st.error(f"Error: {e}")
                finally:
                    # Restore the standard output
                    sys.stdout = old_stdout
                
                # Get the captured output
                output = redirected_output.getvalue()
                
            # Display the output in a text area
            st.text_area("Output:", value=output, height=300)
            st.success('Execution finished!')

elif activity == "Python Turtle Graphics":
    # Python Turtle Graphics Section
    st.markdown("## Python Turtle Graphics")
    show_turtle_window = st.checkbox("Show/Hide Python Turtle Window", value=False)

    if show_turtle_window:
        # Embed Trinket.io Turtle project
        trinket_embed_url = "https://trinket.io/embed/python/f3311da13d"  # Replace with your Trinket.io embed URL
        st.components.v1.iframe(trinket_embed_url, height=1000, scrolling=False)



# Display courses 
for course in courses:
    st.markdown(f"""
    <div class="course-section">
        <h2 class="course-title">{course['title']}</h2>
        <p class="course-description">{course['description']}</p>
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
