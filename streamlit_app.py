import streamlit as st
import tempfile
from pdf_utils import extract_text_from_pdf
from prompt_model import summarize_resume

st.title("📄 Resume Summarizer AI")

uploaded = st.file_uploader("Upload resume (PDF)", type="pdf")

if uploaded:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded.read())
        text = extract_text_from_pdf(tmp_file.name)

    st.text_area("Resume Preview", text, height=250)

    if st.button("Summarize"):
        summary = summarize_resume(text)
        st.json(summary.model_dump())
