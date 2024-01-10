import streamlit as st
from streamlit_ace import st_ace
import subprocess
import os
import uuid

def main():
    # Customizing the page layout, style, and title
    st.set_page_config(page_title="CodeSage by Moshiur", layout="wide")
    
    st.markdown("""
    <style>
    /* Main page style */
    body {
        color: #4F8BF9; /* Primary text color */
        background-color: #E6F0FF; /* Page background color */
    }
    /* Header style */
    .reportview-container .main .block-container {
        padding-top: 5rem;
    }
    /* Editor and button style */
    .st-bc, .st-ae {
        border-color: #4F8BF9;
        background-color: #FFFFFF;
        color: #4F8BF9;
    }
    /* Footer style */
    .footer {
        font-size: 16px;
        font-style: italic;
        color: #4F8BF9;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title and introduction
    st.title("Welcome to CodeSage")
    st.write("Explore and enhance your programming skills. Write and execute your C++ code right here.")

    # YouTube channel link
    st.markdown("For more insights and tutorials, visit [Moshiur's YouTube Channel](https://youtube.com/mhridoy)")

    # Streamlit-ace editor for C++ code
    c_plus_code = st_ace(language="c_cpp", theme="twilight", key="cppEditor")

    if c_plus_code:
        result = execute_cpp_code(c_plus_code)
        st.markdown("#### C++ Code Output:")
        st.code(result, language='bash')

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
