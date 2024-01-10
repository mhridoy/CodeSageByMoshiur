import streamlit as st
from streamlit_ace import st_ace
import subprocess
import os
import uuid

def main():
    # Customizing the page layout and style
    st.set_page_config(page_title="CodeSage by Moshiur", layout="wide")
    
    # Custom CSS for the app
    st.markdown("""
    <style>
    /* Main page style */
    body {
        color: #293241; /* Primary text color */
        background-color: #a8dadc; /* Soft teal background color */
        background-image: linear-gradient(180deg, #a8dadc 0%, #457b9d 100%);
    }
    /* Streamlit components and widgets style */
    .stTextInput, .stButton>button, .stSelectbox, .stSlider {
        background-color: #f1faee;
        border-color: #1d3557;
        color: #1d3557;
    }
    .st-bb, .st-cf {
        color: #1d3557;
    }
    .st-bc, .st-ae {
        border-color: #1d3557;
    }
    /* Header and titles style */
    h1, h2, h3 {
        color: #f4a261;
    }
    /* Footer style */
    .footer {
        font-size: 16px;
        font-style: italic;
        color: #2a9d8f;
    }
    </style>
    """, unsafe_allow_html=True)

    # Page header
    st.title("Welcome to CodeSage")
    st.markdown("#### Enhance your programming journey. Write and execute C++ code in a relaxing environment.")

    # Layout with columns
    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("## Code Editor")
        c_plus_code = st_ace(language="c_cpp", theme="twilight", key="cppEditor")
        prev_code = st.session_state.get('prev_code', '')

        # Execute C++ code when there's a change in the editor content
        if c_plus_code and c_plus_code != prev_code:
            result = execute_cpp_code(c_plus_code)
            st.code(result, language='bash')

        st.session_state['prev_code'] = c_plus_code

    with col2:
        st.markdown("## Programming Tips")
        st.markdown("Explore C++ tips and tricks:")
        tip = st.selectbox("Choose a programming tip to learn more:",
                           ["Select a tip", "Tip 1: Code Efficiency", "Tip 2: Readable Code", "Tip 3: Debugging Strategies"])
        if tip != "Select a tip":
            st.info(f"You selected {tip}. Here's some information on it...")

        st.markdown("## YouTube Channel")
        st.markdown("For more insights and tutorials, visit [Moshiur's YouTube Channel](https://youtube.com/mhridoy)")

def execute_cpp_code(code):
    # Generate a unique file name
    filename = f"temp_code_{uuid.uuid4().hex}.cpp"
    executable = f"temp_code_{uuid.uuid4().hex}"

    try:
        # Write code to a file
        with open(filename, "w") as file:
            file.write(code)

        # Compile the C++ code
        compile_process = subprocess.run(["g++", filename, "-o", executable], capture_output=True, text=True)
        if compile_process.returncode != 0:
            # Compilation failed
            return compile_process.stderr

        # Run the compiled executable
        run_process = subprocess.run([f"./{executable}"], capture_output=True, text=True)
        return run_process.stdout if run_process.returncode == 0 else run_process.stderr

    except Exception as e:
        return str(e)
    finally:
        # Clean up: remove the temporary files
        if os.path.exists(filename):
            os.remove(filename)
        if os.path.exists(executable):
            os.remove(executable)

if __name__ == "__main__":
    main()
