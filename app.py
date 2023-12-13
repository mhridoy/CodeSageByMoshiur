import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title='CodeSage By Moshiur', layout='wide')

# Custom CSS for Styling
st.markdown("""
<style>
    h1 {
        color: #ff6347;
        text-align: center;
    }
    .table {
        margin-left: auto; 
        margin-right: auto;
        border-collapse: collapse;
        width: 80%;
        font-size: 20px;
    }
    .table td, .table th {
        border: 1px solid #ddd;
        padding: 8px;
    }
    .table tr:nth-child(even){background-color: #f2f2f2;}
    .table tr:hover {background-color: #ddd;}
    .table th {
        padding-top: 12px;
        padding-bottom: 12px;
        text-align: center;
        background-color: #4CAF50;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>CodeSage By Moshiur</h1>", unsafe_allow_html=True)

# Data for the Table
data = {
    'Batch': [f'Batch {i+1}' for i in range(13)],
    'Google Colab Link': [f'http://colab.link/batch{i+1}' for i in range(13)]  # Example links
}
df = pd.DataFrame(data)

# Display the Table with Custom Styling
st.markdown(df.to_html(classes='table', escape=False, index=False), unsafe_allow_html=True)

# Additional Interactive Elements (Optional)
st.sidebar.title("Navigation")
selected_batch = st.sidebar.selectbox("Choose a Batch", df['Batch'])
st.sidebar.markdown(f"You selected: {selected_batch}")

# Display Batch Information
st.write(f"Selected Batch: {selected_batch}")
colab_link = df[df['Batch'] == selected_batch]['Google Colab Link'].iloc[0]
st.markdown(f"[Go to Google Colab]({colab_link})")

