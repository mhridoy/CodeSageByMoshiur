import streamlit as st
from streamlit_ace import st_ace
import subprocess
import os
import uuid

def main():
    # Customizing the page layout and style
    st.set_page_config(page_title="CodeSage by Moshiur", layout="wide")

    # Custom CSS for the app
    apply_custom_css()
    

    # Page header
    st.title("Welcome to CodeSage")
    st.markdown("#### Enhance your programming journey in a vibrant and interactive environment.")

    # Layout with tabs
    tab1, tab2, tab3 = st.tabs(["Code Editor", "Programming Tips", "YouTube Channel"])

    with tab1:
        c_plus_code = st_ace(language="c_cpp", theme="monokai", key="cppEditor")
        user_input = st.text_area("Input for your code (if any):", height=100)

        if st.button("Run C++ Code"):
            result = execute_cpp_code(c_plus_code, user_input)
            st.code(result, language='bash')

    with tab2:
        display_programming_tips()

    with tab3:
        display_youtube_channel()
def apply_custom_css():
    st.markdown("""
    <style>
    /* Main page style */
    body {
        color: #023047; /* Primary text color */
        background-color: #8ECAE6; /* Soft blue background */
        background-image: linear-gradient(315deg, #8ECAE6 0%, #BDB2FF 74%);
    }
    /* Streamlit components and widgets style */
    .stTextInput, .stButton>button, .stSelectbox, .stSlider {
        background-color: #FFB4A2;
        border-color: #FFCDB2;
        color: #023047;
    }
    .st-bb, .st-cf {
        color: #023047;
    }
    .st-bc, .st-ae {
        border-color: #FFCDB2;
    }
    /* Header and titles style */
    h1, h2, h3 {
        color: #FFB4A2;
    }
    /* Footer style */
    .footer {
        font-size: 16px;
        font-style: italic;
        color: #FFB4A2;
    }
    </style>
    """, unsafe_allow_html=True)



def execute_cpp_code(code, user_input):
    # Create a temporary file for the source code
    src_filename = f"temp_code_{uuid.uuid4().hex}.cpp"
    executable = f"{src_filename}.exe"

    try:
        with open(src_filename, "w") as src_file:
            src_file.write(code)

        # Compile the C++ code
        compile_process = subprocess.run(["g++", src_filename, "-o", executable], capture_output=True, text=True)
        if compile_process.returncode != 0:
            return compile_process.stderr

        # Run the compiled executable with user input
        run_process = subprocess.run([executable], input=user_input, text=True, capture_output=True)
        return run_process.stdout if run_process.returncode == 0 else run_process.stderr

    finally:
        # Clean up: remove the temporary files
        if os.path.exists(src_filename):
            os.remove(src_filename)
        if os.path.exists(executable):
            os.remove(executable)

def display_programming_tips():
        st.markdown("## Learn with Tips")
        st.markdown("Explore C++ tips and tricks:")
        tip = st.selectbox("Choose a programming tip:",
                           ["Select a tip", "Tip 1: Efficient Code", "Tip 2: Clean Code", "Tip 3: Debugging"])
        if tip != "Select a tip":
            st.info(f"Info on {tip}")

def display_youtube_channel():
        st.markdown("## Explore More on YouTube")
        st.markdown("[Moshiur's YouTube Channel](https://youtube.com/mhridoy)")
        st.video("https://www.youtube.com/watch?v=qsqYEGav6mU")  # Replace with a relevant video link

if __name__ == "__main__":
    main()
