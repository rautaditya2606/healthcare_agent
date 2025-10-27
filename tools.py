from PyPDF2 import PdfReader

def get_pdf_text(pdf_path: str) -> str:
    try:
        reader = PdfReader(pdf_path)
        return "".join(page.extract_text() or "" for page in reader.pages).strip()
    except Exception as e:
        return f"Error extracting text: {e}"

text = get_pdf_text('/home/adityaraut/Downloads/test1.pdf')
print(text)
