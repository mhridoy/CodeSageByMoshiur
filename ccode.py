import streamlit as st
from streamlit_ace import st_ace
import subprocess
import os
import uuid

def main():
    st.title("C++ Integration with Streamlit")

    # Hide the 'Apply cmd+Enter' button using custom CSS
    hide_button_style = """
    <style>
    .st-bc { 
        display: none;
    }
    </style>
    """
    st.markdown(hide_button_style, unsafe_allow_html=True)

    # Streamlit-ace editor for C++ code
    c_plus_code = st_ace(language="c_cpp", theme="twilight", key="cppEditor")

    if st.button("Run C++ Code"):
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
