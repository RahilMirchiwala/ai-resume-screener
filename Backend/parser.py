import pdfplumber
import io

def extract_text_from_pdf(source):

  if isinstance(source,bytes):
    file = io.BytesIO(source)
  else:
    file = source

  text_parts = []

  with pdfplumber.open(file) as pdf:
    for page in pdf.pages:
      page_text = page.extract_text()
      if page_text:
        text_parts.append(page_text)
    
  return "\n".join(text_parts)
  

