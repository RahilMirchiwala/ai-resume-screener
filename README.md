# AI Resume Screener

A tool that helps users check if their skills are a good match for a job description.

## What It Does

Upload a resume PDF and paste a job description. The app returns:
- Extracted skills from the resume
- Extracted skills from the job description  
- A match score (0-100)
- An AI explanation of the match

## How It Works

1. User uploads a PDF resume
2. `parser.py` extracts raw text from the PDF using pdfplumber
3. `extractor.py` sends the text to an LLM which returns a list of skills
4. Same process runs on the job description
5. `matcher.py` normalizes both skill lists (lowercase, remove spaces/symbols)
6. Matched skills = skills present in both lists
7. Missing skills = job skills not found in resume
8. Score formula: `(matched skills / total job skills) * 100`
9. `explainer.py` sends everything to the LLM to generate a human-readable analysis

## Tech Stack

- Python
- FastAPI
- pdfplumber
- Groq API (LLaMA 3)
- HTML/CSS/JavaScript

## How to Run Locally

```bash
git clone https://github.com/RahilMirchiwala/ai-resume-screener
cd ai-resume-screener/Backend
pip install -r requirements.txt
# Add your GROQ_API_KEY to .env file
uvicorn main:app --reload
```

## Live Demo

https://ai-resume-screener-1-hw2o.onrender.com/ui

## What I Would Improve Next

- Semantic matching so "REST APIs" and "RESTful APIs" count as the same skill
- Better scoring that gives partial credit for related skills
