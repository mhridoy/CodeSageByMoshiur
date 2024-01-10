import streamlit as st
import subprocess

st.title("C++ Code Execution Demo")

# Store the code in session state
if 'code' not in st.session_state:
    st.session_state['code'] = ""

code = st.text_area("Write your C++ code here", height=400, value=st.session_state['code'])

if st.button("Run Code"):
    st.session_state['code'] = code  # Update code in session state

    # Assuming you have a pre-compiled executable named "output" in your app directory
    try:
        output = subprocess.check_output(["./output"])
        st.write("Output:")
        st.code(output.decode("utf-8"), language="cpp")
    except subprocess.CalledProcessError as e:
        st.error(f"Error: {e}")
