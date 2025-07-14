# main.py

from fastapi import FastAPI
from api.extract_resume import router as extract_resume

app = FastAPI()
app.include_router(extract_resume, prefix="/api/v1")
