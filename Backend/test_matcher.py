from parser import extract_text_from_pdf
from extractor import extract_skills
from matcher import calculate_match

resume_text = extract_text_from_pdf(r"E:\ML Project\AI Resume Screener\MyResume (Full).pdf")
resume_skills = extract_skills(resume_text,source="resume")

with open("sample_jd.txt","r",encoding="utf-8") as f:
  jd_text = f.read()
jd_skills = extract_skills(jd_text,source="job_description")

result = calculate_match(resume_skills,jd_skills)

print(f"Match Score: {result['Score']}/100")
print(f"\nMatched Skills ({len(result['Matched Skills'])})")
for skill in result['Matched Skills']:
  print(f"  ✓ {skill}")

print(f"\nMissing Skills ({len(result['Missing Skills'])}):")
for skill in result['Missing Skills']:
    print(f"  ✗ {skill}")