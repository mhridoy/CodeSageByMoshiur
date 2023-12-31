import streamlit as st
from fpdf import FPDF

# Function to generate PDF
def create_pdf(context):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Adding personal information
    pdf.cell(200, 10, txt=f"Name: {context['name']}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {context['email']}", ln=True)
    pdf.cell(200, 10, txt=f"Phone Number: {context['phone_number']}", ln=True)

    # Adding Education
    pdf.cell(200, 10, txt="Education:", ln=True)
    for edu in context['education']:
        pdf.cell(200, 10, txt=f"{edu['degree']} from {edu['institution']} - {edu['year']}", ln=True)

    # Adding Work Experience
    pdf.cell(200, 10, txt="Work Experience:", ln=True)
    for exp in context['work_experience']:
        pdf.cell(200, 10, txt=f"{exp['job_title']} at {exp['company']} ({exp['duration']})", ln=True)
        pdf.multi_cell(0, 10, txt=exp['description'])

    # Adding Skills
    pdf.cell(200, 10, txt="Skills:", ln=True)
    pdf.multi_cell(0, 10, txt=", ".join(context['skills']))

    # Adding References
    pdf.cell(200, 10, txt="References:", ln=True)
    for ref in context['references']:
        pdf.cell(200, 10, txt=f"{ref['name']} - {ref['position']}, Contact: {ref['contact']}", ln=True)

    pdf.output("resume.pdf")

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
    # Gather data into context
    context = {
        "name": name,
        "email": email,
        "phone_number": phone_number,
        "education": education,
        "work_experience": work_experience,
        "skills": skills.split(","),
        "references": references
    }

    # Create PDF
    create_pdf(context)

    # Display the payment link
    st.markdown("Please complete the payment to download your resume.")
    st.markdown("[Proceed to Payment](https://shop.bkash.com/codesage-by-moshiur01752175087/pay/bdt20/nCzYqc)", unsafe_allow_html=True)

    # Assume payment is successful for demo purposes
    # In a real application, you should verify the payment
    with open("resume.pdf", "rb") as file:
        st.download_button(label="Download Resume", data=file, file_name="resume.pdf", mime="application/pdf")
