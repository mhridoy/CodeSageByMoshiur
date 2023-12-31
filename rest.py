import streamlit as st
import docxtpl  # Install using: pip install docxtpl
import requests  # For payment status check
import os
# Payment verification function
def verify_payment(payment_id):
    # Replace with your logic to check payment status using bKash API
    response = requests.get(f"https://api.bkash.com/payment/status/{payment_id}")
    return response.json()["status"] == "successful"

template_file = "resume_template.docx"
if not os.path.exists(template_file):
    st.error(f"Template file '{template_file}' not found.")
else:
    resume_template = docxtpl.DocxTemplate(template_file)

# User input fields
st.title("Resume Builder")

with st.form("resume_form"):
    st.write("**Personal Information**")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone_number = st.text_input("Phone Number")

    st.write("**Education**")
    education = []
    for i in range(3):
        degree = st.text_input(f"Degree {i+1}")
        institution = st.text_input(f"Institution {i+1}")
        year = st.text_input(f"Year {i+1}")
        education.append({"degree": degree, "institution": institution, "year": year})

    st.write("**Work Experience**")
    work_experience = []
    for i in range(2):
        job_title = st.text_input(f"Job Title {i+1}")
        company = st.text_input(f"Company {i+1}")
        duration = st.text_input(f"Duration {i+1}")
        description = st.text_area(f"Description {i+1}")
        work_experience.append({"job_title": job_title, "company": company, "duration": duration, "description": description})

    st.write("**Skills**")
    skills = st.text_area("Skills (comma-separated)")

    st.write("**References**")
    references = []
    for i in range(2):
        name = st.text_input(f"Name {i+1}")
        position = st.text_input(f"Position {i+1}")
        contact = st.text_input(f"Contact {i+1}")
        references.append({"name": name, "position": position, "contact": contact})

    submitted = st.form_submit_button("Submit")

if submitted:
    # Render resume content
    context = {
        "name": name,
        "email": email,
        "phone_number": phone_number,
        "education": education,
        "work_experience": work_experience,
        "skills": skills.split(","),
        "references": references
    }
    resume_template.render(context)

    # Generate resume file
    resume_file = "resume.docx"
    resume_template.save(resume_file)

    # Redirect to payment gateway
    st.session_state["payment_required"] = True
    st.session_state["resume_file"] = resume_file
    st.experimental_redirection("https://shop.bkash.com/codesage-by-moshiur01752175087/pay/bdt20/nCzYqc")

# Payment verification and download
if st.session_state.get("payment_required"):
    payment_id = st.session_state.get("payment_id")  # Get payment ID from URL or user input
    if payment_id and verify_payment(payment_id):
        resume_file = st.session_state.get("resume_file")
        st.download_button(label="Download Resume", data=resume_file, file_name="resume.docx")
        st.session_state.clear()  # Clear session state
    else:
        st.error("Payment verification failed. Please try again.")
