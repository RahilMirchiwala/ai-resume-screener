import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_skills(text,source = "resume"):

  if source == "resume":
    prompt = f"""Extract all technical and professional skills from this resume.

    Resume text:
    {text}

    Return ONLY a JSON array of skills. Nothing else. No explanation.
    Example: ["Python", "Machine Learning", "React", "SQL"]"""
    
  else:
    prompt = f"""Extract all required skills from this job description.

    Job description:
    {text}

    Return ONLY a JSON array of skills. Nothing else. No explanation.
    Example: ["Python", "Docker", "FastAPI", "AWS"]"""

  response = client.chat.completions.create(
  model="llama-3.1-8b-instant",
  messages=[{"role": "user", "content": prompt}]
  )

  raw = response.choices[0].message.content.strip()
  skills = json.loads(raw)
  return skills