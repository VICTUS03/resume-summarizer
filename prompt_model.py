from pydantic import BaseModel
from groq_llm import query_groq
import json
import re

class ResumeSummary(BaseModel):
    name: str
    skills: list[str]
    experience_years: int
    summary: str

def summarize_resume(resume_text: str) -> ResumeSummary:
    prompt = """
Extract the following from this resume:
- Name
- Key Skills (as a list)
- Total Years of Experience (as an integer)
- One-line summary

Return the result in this exact JSON format, with no extra text:

{
  "name": "...",
  "skills": ["...", "..."],
  "experience_years": ...,
  "summary": "..."
}

Resume:
""" + resume_text

    result = query_groq(prompt)

    # Extract JSON from the response using regex
    try:
        json_match = re.search(r'\{[\s\S]*\}', result)
        if not json_match:
            raise ValueError("No JSON object found in response.")
        json_string = json_match.group()
        parsed = json.loads(json_string)
        return ResumeSummary(**parsed)

    except Exception as e:
        print("❌ Failed to extract/parse JSON:")
        print("----- Raw result -----")
        print(result)
        print("----- Error -----")
        print(e)
        raise
