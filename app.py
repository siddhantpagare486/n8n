import requests
import streamlit as st
import google.generativeai as genai
from io import BytesIO
from docx import Document
import PyPDF2

# -----------------------------
# CONFIGURE GEMINI API
# -----------------------------
genai.configure(api_key="GEMINI_API_KEY")
model = genai.GenerativeModel("models/gemini-2.5-flash")

# -----------------------------
# STREAMLIT APP
# -----------------------------
st.title("AI Document Orchestrator")

file = st.file_uploader("Upload a document (txt, PDF, DOCX)")

def extract_text(file):
    """Extract text from txt, pdf, or docx"""
    if file.name.endswith(".txt"):
        try:
            text = file.read().decode("utf-8")
        except UnicodeDecodeError:
            file.seek(0)
            text = file.read().decode("latin-1")
        return text
    elif file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    elif file.name.endswith(".docx"):
        doc = Document(file)
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text
    else:
        return None

# -----------------------------
# PROCESS FILE
# -----------------------------
if file:
    st.write("File uploaded successfully")
    text = extract_text(file)

    if text:
        # Generate summary using Gemini AI
        prompt = f"Summarize this document: {text}"
        response = model.generate_content(prompt)
        st.subheader("Summary:")
        st.write(response.text)

        # Button to send summary to n8n webhook
        if st.button("Send Summary via Email"):
            webhook_url = "N8N_WEBHOOK_URL"
            data = {
                "filename": file.name,
                "summary": response.text,
                "to": "siddhantpagare913@gmail.com"  # optional: dynamic email from workflow
            }
            try:
                r = requests.post(webhook_url, json=data)
                if r.status_code == 200:
                    st.success("Summary sent successfully!")
                else:
                    st.error("Failed to send summary. Check n8n webhook.")
            except Exception as e:
                st.error(f"Error sending to webhook: {e}")

    else:
        st.error("Unsupported file type. Please upload .txt, .pdf, or .docx")