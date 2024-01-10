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
        color: #342E4C; /* Primary text color */
        background-color: #E0BBE4; /* Gradient background color */
        background-image: linear-gradient(315deg, #E0BBE4 0%, #957DAD 74%);
    }
    /* Streamlit components and widgets style */
    .stTextInput, .stButton>button, .stSelectbox, .stSlider {
        background-color: #FFC8DD;
        border-color: #FFAFCC;
        color: #6A2C70;
    }
    .st-bb, .st-cf {
        color: #6A2C70;
    }
    .st-bc, .st-ae {
        border-color: #FFAFCC;
    }
    /* Header and titles style */
    h1, h2, h3 {
        color: #B28DFF;
    }
    /* Footer style */
    .footer {
        font-size: 16px;
        font-style: italic;
        color: #B28DFF;
    }
    </style>
    """, unsafe_allow_html=True)

    # Page header
    st.title("CodeSage By Moshiur এ স্বাগতম")
    st.markdown("#### প্রোগ্রামিং যাত্রায় আপনার সঙ্গী। C++ কোডিং এখানেই লিখুন এবং চালান।")

    # Layout with columns
    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("## কোড এডিটর")
        c_plus_code = st_ace(language="c_cpp", theme="twilight", key="cppEditor")
        prev_code = st.session_state.get('prev_code', '')

        # Execute C++ code when there's a change in the editor content
        if c_plus_code and c_plus_code != prev_code:
            result = execute_cpp_code(c_plus_code)
            st.code(result, language='bash')

        st.session_state['prev_code'] = c_plus_code

    with col2:
        st.markdown("## প্রোগ্রামিং টিপস")
        st.markdown("বাংলায় C++ টিপস:")
        tip = st.selectbox("টিপ নির্বাচন করুন:", 
                           ["টিপ নির্বাচন করুন", "টিপ ১: কোড দক্ষতা", "টিপ ২: পরিষ্কার কোড", "টিপ ৩: ডিবাগিং কৌশল"])
        if tip == "টিপ ১: কোড দক্ষতা":
            st.info("দক্ষ কোড লেখার জন্য...")
        elif tip == "টিপ ২: পরিষ্কার কোড":
            st.info("পরিষ্কার কোড লেখা নিশ্চিত করে...")
        elif tip == "টিপ ৩: ডিবাগিং কৌশল":
            st.info("ডিবাগিং করার সময়...")

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
