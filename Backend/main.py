from fastapi import FastAPI,UploadFile,File,Form
from parser import extract_text_from_pdf
from extractor import extract_skills
from matcher import calculate_match
from explainer import generate_explanation
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AI Resume Screener API is running"}

@app.post("/analyze")
async def analyze(
  resume: UploadFile = File(...),
  job_description: str = Form(...)
):
  
  pdf_bytes = await resume.read()

  resume_text = extract_text_from_pdf(pdf_bytes)

  resume_skills = extract_skills(resume_text,source="resume")
  job_skills = extract_skills(job_description,source="job_description")

  result = calculate_match(resume_skills,job_skills)

  explanation = generate_explanation(
    resume_skills=resume_skills,
    job_skills=job_skills,
    matched_skills=result["Matched Skills"],
    missing_skills=result["Missing Skills"],
    score=result["Score"]
  )

  return {
    "score": result['Score'],
    "matched_skills": result['Matched Skills'],
    "missing_skills": result['Missing Skills'],
    "explanation": explanation
  }