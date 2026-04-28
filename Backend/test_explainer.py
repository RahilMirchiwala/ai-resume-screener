from parser import extract_text_from_pdf
from extractor import extract_skills
from matcher import calculate_match
from explainer import generate_explanation

resume_text = extract_text_from_pdf(r"E:\ML Project\AI Resume Screener\MyResume (Full).pdf")
resume_skills = extract_skills(resume_text,source="resume")

with open("sample_jd.txt","r",encoding="utf-8") as f:
  jd_text = f.read()
job_skills = extract_skills(jd_text,source="job_description")

result = calculate_match(resume_skills,job_skills)
# print(result)

explanation = generate_explanation(
  resume_skills=resume_skills,
  job_skills=job_skills,
  matched_skills=result["Matched Skills"],
  missing_skills=result["Missing Skills"],
  score=result["Score"]
)

print(f"Score: {result['Score']}/100")
print(f"\nMatched: {result['Matched Skills']}")
print(f"\nMissing: {result['Missing Skills']}")
print(f"\n--- AI Explanation ---")
print(explanation)