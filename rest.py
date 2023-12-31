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
    # ... (Your existing code for user inputs)

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
