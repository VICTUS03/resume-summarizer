from pdf_utils import extract_text_from_pdf
from prompt_model import summarize_resume

pdf_path = r"C:\Users\pratik p kakade\Downloads\Hrishikesh_Kakade_Resume.pdf"  # Replace with your file
resume_text = extract_text_from_pdf(pdf_path)

summary = summarize_resume(resume_text)
print("\n📌 Structured Resume Summary:\n")
print(summary.model_dump_json(indent=2))
