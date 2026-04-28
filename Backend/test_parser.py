from parser import extract_text_from_pdf

text = extract_text_from_pdf(r"E:\ML Project\AI Resume Screener\MyResume (Full).pdf")
print(text[:500])
print("-----")
print("Total Charcters:",len(text))