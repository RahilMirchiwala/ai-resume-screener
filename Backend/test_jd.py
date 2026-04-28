from extractor import extract_skills

with open("sample_jd.txt", "r", encoding="utf-8") as f:
  jd_text = f.read()

jd_skills = extract_skills(jd_text,source="job_description")

print("Job Required Skills:")
for skill in jd_skills:
  print(f"- {skill}")

print(f"Total Skills Required: {len(jd_skills)}")