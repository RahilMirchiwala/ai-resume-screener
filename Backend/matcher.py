def normalize(skill):
  skill = skill.lower()
  skill = skill.replace(" ", "")
  skill = skill.replace(".", "")
  skill = skill.replace("-", "")
  skill = skill.replace("_", "")
  return skill

def calculate_match(resume_skills,job_skills):
  resume_normalized = {normalize(s): s for s in resume_skills }
  job_normalized = {normalize(s): s for s in job_skills }

  matched_keys = set(resume_normalized.keys()) & set(job_normalized.keys())
  missing_keys = set(job_normalized.keys()) - set(resume_normalized.keys())

  matched_skills = [job_normalized[k] for k in matched_keys]
  missing_skills = [job_normalized[k] for k in missing_keys]

  score = round(len(matched_keys)/len(job_normalized) * 100)

  return {
    "Score":score,
    "Matched Skills":sorted(matched_skills),
    "Missing Skills":sorted(missing_skills)
  }
