import fitz  # PyMuPDF
import spacy
import streamlit as st
# from langchain.chat_models import ChatOpenAI
# from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceHub

from langchain.prompts import PromptTemplate

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")  # Read uploaded file
    text = "\n".join([page.get_text() for page in doc])  # Extract text from each page
    return text

# Function to extract named entities
def extract_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

# Initialize LangChain LLM
# llm = ChatOpenAI(model_name="gpt-4", openai_api_key="YOUR_OPENAI_KEY")
llm = HuggingFaceHub(
    repo_id="mistralai/Mistral-7B-Instruct",
    huggingfacehub_api_token=st.secrets["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"],
    model_kwargs={"temperature": 0.7, "max_length": 500}
)

# Function to analyze job fit
def analyze_fit(resume_text, job_desc):
    prompt = PromptTemplate(
        input_variables=["resume", "job"],
        template="Compare the resume:\n{resume}\n with job description:\n{job}\n and rate the match on a scale of 1-10."
    )
    return llm(prompt.format(resume=resume_text, job=job_desc))
