import streamlit as st
import os
from admin import extract_text_from_pdf,extract_entities,analyze_fit


# Streamlit UI
st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description")

if uploaded_file and job_desc:
    resume_text = extract_text_from_pdf(uploaded_file)
    fit_score = analyze_fit(resume_text, job_desc)
    st.subheader("Results")
    st.write(f"Match Score: {fit_score}")

# st.divider()  # Adds a horizontal line

# author = st.write("Developed By : Ankush Pawar")
st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #000000;
            text-align: center;
            padding: 10px;
            font-size: 14px;
        }
    </style>
    <div class="footer">
        <p>Developed by <b> Ankush Pawar</b></p>
    </div>
    """,
    unsafe_allow_html=True
)

# Assist in the collection processing and management of clinical data to ensure accuracy and compliance.
# Utilize Generative AI techniques to enhance data processing and analysis workflows.
# Collaborate with cross-functional teams to support research and development activities.
# Ensure timely and accurate PV case processing in accordance with regulatory requirements.
# Provide support in the preparation and submission of regulatory documents.
# Monitor and track data quality issues and implement corrective actions as needed.
# Conduct data validation and verification to maintain data integrity.
# Assist in the development and maintenance of standard operating procedures.
# Participate in training sessions to stay updated with the latest industry trends and technologies.
# Support the implementation of process improvements to enhance efficiency and productivity.
# Communicate effectively with team members and stakeholders to ensure project goals are met.
# Contribute to the development of innovative solutions to improve data management processes.
# Maintain confidentiality and security of sensitive information.