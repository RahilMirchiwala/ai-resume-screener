from parser import extract_text_from_pdf
from extractor import extract_skills

# Step 1: Get resume text (your work from Day 1)
resume_text = extract_text_from_pdf(r"E:\ML Project\AI Resume Screener\MyResume (Full).pdf")

# Step 2: Extract skills
skills = extract_skills(resume_text, source="resume")

# Step 3: Print result
print("Extracted Skills:")
for skill in skills:
    print(f"  - {skill}")

print(f"\nTotal skills found: {len(skills)}")