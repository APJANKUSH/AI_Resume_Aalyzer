import fitz  # PyMuPDF
import spacy
import streamlit as st
import subprocess
from langchain_community.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate

# Load API key securely
api_key = st.secrets["HUGGINGFACEHUB_API_TOKEN"]

# Load NLP model

def load_spacy_model(model_name):
    try:
        return spacy.load(model_name)
    except OSError:
        subprocess.run(["python", "-m", "spacy", "download", model_name])
        return spacy.load(model_name)
nlp = load_spacy_model("en_core_web_sm")
# nlp = spacy.load("en_core_web_sm")

# Function to extract text from PDF
# def extract_text_from_pdf(pdf_path):
#     doc = fitz.open(pdf_path)  # Open file from path
#     text = "\n".join([page.get_text() for page in doc])  # Extract text from each page
#     return text

def extract_text_from_pdf(pdf_path):
    with fitz.open(stream=pdf_path.read(), filetype="pdf") as doc:
        text = "\n".join([page.get_text() for page in doc])
    return text

# Function to extract named entities
def extract_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

# Initialize LangChain LLM
llm = HuggingFaceHub(
    # repo_id="meta-llama/Llama-2-7b-chat-hf",
    repo_id = "declare-lab/flan-alpaca-base",
    # repo_id="google/flan-t5-large",
    huggingfacehub_api_token=api_key,
    model_kwargs={"temperature": 0.7, "max_length": 512},
    task="text2text-generation"
)

# Function to analyze job fit
def analyze_fit(resume_text, job_desc):
    prompt = PromptTemplate(
        input_variables=["resume", "job"],
        template="Compare the resume:\n{resume}\n with job description:\n{job}\n and rate the match on a scale of 1-10."
    )
    return llm(prompt.format(resume=resume_text, job=job_desc))
