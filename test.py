import streamlit as st
import pandas as pd
import sys
import io
import streamlit_ace as st_ace


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

# Enhanced color scheme
colors = {
    'background': 'linear-gradient(135deg, #E6FDFC, #FFFAF3)',
    'primary': '#31708E',
    'secondary': '#A3C4BC',
    'accent': '#FFD580',
    'text': '#252422',
    'footer_bg': '#31708E',
    'footer_text': '#FFFAF3',
    'table_bg': '#FFFFFF',
    'table_text': '#31708E',
    'row_highlight': '#E6FDFC'
}

# Custom styles
st.markdown(f"""
<style>
    /* Global Styles */
    body {{
        font-family: 'Georgia', serif;
        background: {colors['background']};
        color: {colors['text']};
    }}

    h1, h2 {{
        font-family: 'Helvetica', sans-serif;
        margin: 0.5em 0;
    }}

    h1 {{
        color: {colors['primary']};
        font-size: 2.5em;
    }}

    h2 {{
        color: {colors['secondary']};
        font-size: 2em;
    }}

    /* Enhanced Button Style */
    .stButton > button {{
        border: none;
        border-radius: 20px;
        background-color: {colors['accent']};
        color: {colors['text']};
        padding: 0.5rem 1rem;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        transition: background-color 0.3s, transform 0.3s;
    }}

    .stButton > button:hover {{
        background-color: {colors['primary']};
        color: {colors['footer_text']};
        transform: translateY(-2px);
    }}

    /* Responsive Design Adjustments */
    @media (max-width: 768px) {{
        .block-container {{
            padding: 2rem;
        }}
    }}

      /* Enhanced Table Style */
    .stDataFrame, .stTable {{
        border-radius: 8px;
        overflow: hidden;
    }}

    .dataframe th {{
        background-color: {colors['secondary']};
        color: {colors['table_text']};
    }}

    .dataframe td {{
        background-color: {colors['table_bg']};
        color: {colors['text']};
        padding: 12px;
    }}

    .dataframe tr:nth-of-type(odd) {{
        background-color: {colors['row_highlight']};
    }}

    /* Adjusting the table header */
    .dataframe thead th {{
        color: {colors['footer_text']};
        font-size: 1em;
    }}

    /* Additional styles for responsive and interactive elements */
    /* ... */
</style>
""", unsafe_allow_html=True)
# Header
st.markdown(f'<h1><img src="https://i.imgur.com/4UZzJwD.png" width="50"> Dreamers Academy - Track 3 | CodeSage By Moshiur</h1>', unsafe_allow_html=True)

# Load the schedule data
schedule_df = load_schedule()

# Main content area
col1, col2 = st.columns([3, 2])
with col1:
       st.dataframe(schedule_df.style.set_properties(**{
        'background-color': colors['table_bg'],
        'color': colors['text'],
        'border-radius': '8px',
        'padding': '12px'
    }))

with col2:
    st.markdown('<h2>Best Homework of the Month 🌟 Sababah Subah</h2>', unsafe_allow_html=True)
    # Replace with the actual image URL or path
    st.image('best_homework.png', caption='Incredible work by our star coder!', use_column_width=True)
    st.write("Code Link : https://trinket.io/turtle/f3311da13d")

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

    # Create a visually appealing code editor with rounded corners and a soft glow
    st.write("""
    <div class="custom-code-editor" style="border-radius: 15px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    """, unsafe_allow_html=True)
    
    user_code = st.text_area("Write your Python code here:", height=400, placeholder="def hello_world():\n    print('Hello, beautiful world!')")

    
    # Button to run the code with a captivating hover effect
    if st.button("Run Code ", style="border-radius: 20px; background-color: #95A5A6; color: #252422; transition: all 0.3s;"):
        # Capture the standard output
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
    
        try:
            # Execute the user's code
            exec(user_code)
        except Exception as e:
            st.error(f"Error: {e}")
        finally:
            # Restore the standard output
            sys.stdout = old_stdout
    
        # Get the captured output
        output = redirected_output.getvalue()
    
        # Display output with a subtle highlight
        st.markdown(f"""
        <div class="output-section" style="border-radius: 10px; padding: 15px; background-color: #F8F5F1; color: #495464;">
        `{output}`
        </div>
        """, unsafe_allow_html=True)
    
    st.write("</div>", unsafe_allow_html=True)

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
