from PyPDF2 import PdfReader

class PDFTextExtractor:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.text = self._extract_text()

    def _extract_text(self) -> str:
        try:
            return "".join(page.extract_text() or "" for page in PdfReader(self.pdf_path).pages).strip()
        except Exception as e:
            return f"Error extracting text: {e}"

    def run(self) -> str:
        return self.text


def get_pdf_tool(pdf_path: str) -> PDFTextExtractor:
    return PDFTextExtractor(pdf_path)


if __name__ == "__main__":
    tool = get_pdf_tool('/home/adityaraut/Downloads/test2.pdf')
    print(tool.run()[:500] + "...")
