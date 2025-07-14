# tools/pdf_search_tool.py

import fitz  # PyMuPDF

class PDFSearchTool:
    name = "PDF Text Extractor"
    description = "Reads a PDF file and extracts all text for further processing."

    def _run(self, file_path: str) -> str:
        try:
            text = ""
            with fitz.open(file_path) as doc:
                for page in doc:
                    text += page.get_text()
            return text
        except Exception as e:
            return f"Error reading PDF: {str(e)}"

def extract_text_from_pdf(file_path: str) -> str:
    tool = PDFSearchTool()
    return tool._run(file_path)
