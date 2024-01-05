import streamlit as st
import subprocess
import sys
import time
import pandas as pd
import random
import streamlit.components.v1 as components

# JavaScript to prompt for full-screen
fullscreen_script = """
<script>
document.addEventListener("DOMContentLoaded", function(){
    if (confirm("Click OK to go into full-screen mode for the exam.")) {
        document.documentElement.requestFullscreen();
    }
});
</script>
"""

components.html(fullscreen_script, height=0)
# Function to run Python code
def run_python_code(code):
    result = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
    return result.stdout if result.stdout else result.stderr

# User Authentication
def check_user(username):
    # Example check (replace with a real user check in a real scenario)
    return username in ['student1', 'student2', 'student3']

# Streamlit app
st.title('Python Coding Exam')

# User login
username = st.sidebar.text_input("Username")
if username:
    if check_user(username):
        st.sidebar.success("Logged in as {}".format(username))

        # Exam timer
        exam_duration = 1800  # 30 minutes in seconds
        if 'start_time' not in st.session_state:
            st.session_state.start_time = time.time()

        elapsed_time = time.time() - st.session_state.start_time
        if elapsed_time < exam_duration:
            st.sidebar.write("Time remaining: {} seconds".format(int(exam_duration - elapsed_time)))

            # Questions
            questions = [
                "1. Write a Python function to calculate the factorial of a number.",
                "2. Create a Python function that takes a list and returns a new list with unique elements of the first list.",
                "3. Write a Python program to find the sum of all numbers in a list."
            ]

            random_question = random.choice(questions)
            st.subheader('Question')
            st.write(random_question)

            # Code editor
            code = st.text_area("Write your code here:", height=200)

            # Button to run the code
            if st.button('Run Code'):
                output = run_python_code(code)
                st.subheader('Output')
                st.text(output)
        else:
            st.error("Time's up! Please submit your exam.")
    else:
        st.sidebar.error("Invalid username")
