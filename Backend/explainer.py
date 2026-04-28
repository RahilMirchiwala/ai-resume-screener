from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

def generate_explanation(resume_skills,job_skills,matched_skills,missing_skills,score):
  
  prompt = f"""You are a senior technical recruiter. Analyze this candidate's match.

  Match Score: {score}/100
  Candidate Skills: {", ".join(resume_skills)}
  Required Job Skills: {", ".join(job_skills)}
  Matched Skills: {", ".join(matched_skills)}
  Missing Skills: {", ".join(missing_skills)}
  
  Write a 3 paragraph analysis:
  1. Overall fit based on the score
  2. Key strengths of this candidate
  3. What they should learn to improve their chances
  
  Be direct and specific. No bullet points. Plain paragraphs only."""

  response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": prompt}]
  )

  return response.choices[0].message.content.strip()