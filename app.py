import streamlit as st
import os
from admin import extract_text_from_pdf, extract_entities, analyze_fit

# Streamlit UI
st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description")

if uploaded_file is not None and job_desc.strip():  # Check if file is uploaded and job_desc is not empty
    # with open("temp_resume.pdf", "wb") as f:
    #     f.write(uploaded_file.read())  # Save file temporarily

    resume_text = extract_text_from_pdf(uploaded_file)  # Pass file path instead of Streamlit object
    fit_score = analyze_fit(resume_text, job_desc)

    st.subheader("Results")
    st.write(f"Match Score: {fit_score}")

# Footer
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
        <p>Developed by <b>Ankush Pawar</b></p>
    </div>
    """,
    unsafe_allow_html=True
)
