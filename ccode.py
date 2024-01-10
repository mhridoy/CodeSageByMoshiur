import streamlit as st
from streamlit_ace import st_ace
import subprocess
import os
import uuid

def main():
    # Customizing the page layout and style
    st.set_page_config(page_title="CodeSage by Moshiur", layout="wide")
    st.markdown("""
    <style>
    .main {
        background-color: #F5F5F5;
    }
    .st-bc { 
        display: none;
    }
    h1 {
        color: #0E6BA8;
    }
    .footer {
        font-size: 16px;
        font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title and introduction
    st.title("CodeSage by Moshiur")
    st.write("Welcome to CodeSage, a platform dedicated to enhancing your programming journey. "
             "Here, you can write and run your C++ code directly in the browser. "
             "This tool is designed to provide a seamless coding experience.")

    # YouTube channel link
    st.markdown("Check out my YouTube channel for more programming insights and tutorials: "
                "[Moshiur's YouTube Channel](https://youtube.com/mhridoy)")

    # Streamlit-ace editor for C++ code
    c_plus_code = st_ace(language="c_cpp", theme="twilight", key="cppEditor")

    if c_plus_code:
        result = execute_cpp_code(c_plus_code)
        st.text("C++ Code Output:")
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
