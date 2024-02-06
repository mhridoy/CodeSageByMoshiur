import streamlit as st
import pandas as pd
import sys
import io
from streamlit_ace import st_ace
# Function to load schedule data from the Excel file
def load_schedule():
    sheet_id = "1MyF5yRHgvu1JqqJljTQSo6GDhvpPcezU_aSrXYd90aM"
    sheet_name = "sheet"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    df = pd.read_csv(url, dtype=str).fillna("")
    #file_path = 'schedule04.xlsx'  # Ensure this path is correct
    return df

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
# Function to display class schedule
def display_schedule():
    # Connect to the first Google Sheet
    sheet_id1 = "1MyF5yRHgvu1JqqJljTQSo6GDhvpPcezU_aSrXYd90aM"
    sheet_name1 = "sheet01"
    url1 = f"https://docs.google.com/spreadsheets/d/{sheet_id1}/gviz/tq?tqx=out:csv&sheet={sheet_name1}"
    df1 = pd.read_csv(url1, dtype=str).fillna("")
    selected_schedule_df1 = df1.iloc[:, :3]

    # Connect to the second Google Sheet
    sheet_id2 = "1MyF5yRHgvu1JqqJljTQSo6GDhvpPcezU_aSrXYd90aM"
    sheet_name2 = "sheet02"
    url2 = f"https://docs.google.com/spreadsheets/d/{sheet_id2}/gviz/tq?tqx=out:csv&sheet={sheet_name2}"
    df2 = pd.read_csv(url2, dtype=str).fillna("")
    selected_schedule_df2 = df2.iloc[:, :3]

    # Create two columns in the Streamlit app
    col1, col2 = st.columns(2)

    # Display the first dataframe in the first column
    with col1:
        st.markdown('<h2>Level 1 (Python) Schedule 📚</h2>', unsafe_allow_html=True)
        st.dataframe(selected_schedule_df1.style.set_properties(**{
            'background-color': colors['background'],
            'color': colors['text']
        }))

    # Display the second dataframe in the second column
    with col2:
        st.markdown('<h2>Level 2 (Web Design) Schedule 📚</h2>', unsafe_allow_html=True)
        st.dataframe(selected_schedule_df2.style.set_properties(**{
            'background-color': colors['background'],
            'color': colors['text']
        }))

# Function to display best homework
def display_homework():
    # Connect to the Google Sheet
    sheet_id = "1MyF5yRHgvu1JqqJljTQSo6GDhvpPcezU_aSrXYd90aM"
    sheet_name = "sheet03"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    df = pd.read_csv(url, dtype=str).fillna("")

    # Display the title
    st.markdown('<h2>Best Homework of the Month 🌟</h2>', unsafe_allow_html=True)

    # Create three columns in the Streamlit app
    col1, col2, col3 = st.columns(3)

    # Display the images in the columns
    for i in range(0, len(df), 3):
        with col1:
            if i < len(df):
                st.image(df.loc[i, 'Image Link'], caption=df.loc[i, 'Name'], use_column_width=True)
                st.markdown(f"Code Link {df.loc[i, 'Code Link']}")
        with col2:
            if i+1 < len(df):
                st.image(df.loc[i+1, 'Image Link'], caption=df.loc[i+1, 'Name'], use_column_width=True)
                st.markdown(f"Code Link {df.loc[i, 'Code Link']}")
        with col3:
            if i+2 < len(df):
                st.image(df.loc[i+2, 'Image Link'], caption=df.loc[i+2, 'Name'], use_column_width=True)
                st.markdown(f"Code Link {df.loc[i, 'Code Link']}")

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
def web_editor():
    web_editor_url = "https://moshiur.pythonanywhere.com"
    st.components.v1.iframe(web_editor_url, height=1000, scrolling=True)
def web01():
    # Custom CSS to inject into the page for a hacker-like aesthetic
    custom_css = """
    <style>

        .caption {
            color: #00ff00;
            font-style: italic;
        }
        a:link, a:visited {
            color: #dddddd;
            background-color: transparent;
            text-decoration: none;
        }
        a:hover, a:active {
            color: #ffffff;
            background-color: transparent;
            text-decoration: underline;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    # Title for your link display with hacker aesthetic
    st.title('👾 Check Out My Web Editor! 👾')

    # Description or any additional text you want to show
    st.markdown("""
    Dive into the world of coding with a design that resonates with **hacker vibes**. Click the link below to start your journey!
    """, unsafe_allow_html=True)

    # Displaying the image with a hacker vibes design
    hacker_image_url = 'https://i.ibb.co/dWHhhxW/Screenshot-2024-02-06-at-1-25-29-PM.png'
    st.image(hacker_image_url, caption='Hacker Vibes Design', use_column_width=True)

    # Displaying the link to your web editor with a custom button
    editor_link = 'http://codesage.pythonanywhere.com'
    st.markdown(f'<a href="{editor_link}" target="_blank"><button style="color: #0f0f0f; background-color: #00ff00; border: none; border-radius: 4px; padding: 10px 24px; font-size: 20px; cursor: pointer;">Visit My Web Editor</button></a>', unsafe_allow_html=True)

    # Optionally, add more interactive or informative elements here

    # Displaying the link to your web editor
    editor_link = 'http://codesage.pythonanywhere.com'
    st.markdown(f'### [Visit My Web Editor]({editor_link})')

    
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
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Schedule", "Homework", "Python Editor", "Turtle Graphics", "Web Editor Simple", "Web Editor Ultimate"])

with tab1:
    display_schedule()

with tab2:
    display_homework()

with tab3:
    python_editor()

with tab4:
    python_turtle_graphics()
with tab5:
    web_editor()
with tab6:
    web01()
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
