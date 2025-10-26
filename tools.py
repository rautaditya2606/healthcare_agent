from crewai_tools import PDFSearchTool

def get_pdf_tool(pdf_path):
    return PDFSearchTool(pdf=pdf_path)
