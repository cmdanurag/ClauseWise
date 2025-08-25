import os
from fastapi import UploadFile, HTTPException
from src.utils.constants import SupportedFileTypes, ALLOWED_EXTENSIONS
from PyPDF2 import PdfReader
import docx


class TextExtractionService:
    def __init__(self):
        pass

    async def process_document(self, file: UploadFile):
        """Validate and extract text from an uploaded document."""
        ext = os.path.splitext(file.filename)[1].lower()

        if ext not in ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=400,
                detail=f"Unsupported file format: {ext}. Allowed: {ALLOWED_EXTENSIONS}"
            )

        if file.content_type == SupportedFileTypes.PDF:
            return {"text": await self._extract_pdf(file)}

        elif file.content_type == SupportedFileTypes.DOCX:
            return {"text": await self._extract_docx(file)}

        elif file.content_type == SupportedFileTypes.TXT:
            return {"text": await self._extract_txt(file)}

        else:
            raise HTTPException(
                status_code=400,
                detail=f"Unsupported content type: {file.content_type}"
            )

    async def _extract_pdf(self, file: UploadFile) -> str:
        reader = PdfReader(file.file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text.strip()

    async def _extract_docx(self, file: UploadFile) -> str:
        doc = docx.Document(file.file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text.strip()

    async def _extract_txt(self, file: UploadFile) -> str:
        contents = await file.read()
        return contents.decode("utf-8").strip()
