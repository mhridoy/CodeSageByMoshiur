import streamlit as st
import subprocess
import os

# Function to compile and run C++ code
def run_cpp_code(code):
    # Write code to temporary file
    with open("temp.cpp", "w") as file:
        file.write(code)

    # Compile the C++ program
    compile_process = subprocess.run(["g++", "temp.cpp", "-o", "temp"], capture_output=True, text=True)
    if compile_process.returncode != 0:
        return compile_process.stderr

    # Run the compiled program
    run_process = subprocess.run(["./temp"], capture_output=True, text=True)
    return run_process.stdout if run_process.returncode == 0 else run_process.stderr

# Streamlit UI
st.title("C++ Code Editor")

# Text area for code input
code = st.text_area("Enter your C++ code here:", placeholder="// Your C++ code")

# Button to run code
if st.button("Run Code"):
    if code.strip() != "":
        # Run the C++ code
        output = run_cpp_code(code)
        st.text_area("Output:", value=output, height=300)
    else:
        st.error("Please enter some code.")

# Clean up temporary files
if os.path.exists("temp.cpp"):
    os.remove("temp.cpp")
if os.path.exists("temp"):
    os.remove("temp")
