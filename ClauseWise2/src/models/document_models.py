# src/models/document_models.py
from pydantic import BaseModel

class DocumentUploadRequest(BaseModel):
    text: str

class DocumentAnalysisResponse(BaseModel):
    analyzed_text: str
