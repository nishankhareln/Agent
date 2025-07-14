# api/extract_resume.py

from fastapi import APIRouter, UploadFile, File
import tempfile
import shutil
from tools.pdf_search_tool import extract_text_from_pdf
from core.vector_store import create_vector_index
from agents.extractor import extract_structured_resume

router = APIRouter()

@router.post("/extract")
async def extract_resume_data(file: UploadFile = File(...)):
    try:
        # Save the uploaded file to a temp location
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            shutil.copyfileobj(file.file, temp_file)
            temp_file_path = temp_file.name

        # Extract raw text from PDF
        raw_text = extract_text_from_pdf(temp_file_path)

        # Create vector index
        create_vector_index(raw_text)

        # Extract structured info
        structured_data = extract_structured_resume()

        return {"raw_text": raw_text, "structured_data": structured_data}

    except Exception as e:
        return {"error": str(e)}
