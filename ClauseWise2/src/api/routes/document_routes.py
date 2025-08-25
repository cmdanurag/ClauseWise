from fastapi import APIRouter, UploadFile, File, HTTPException
from src.services.text_extraction_service import TextExtractionService
from src.utils.constants import SupportedFileTypes

router = APIRouter()

document_service = TextExtractionService()

@router.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):
    """Upload and analyze a document."""
    #  Validate file type
    if file.content_type not in SupportedFileTypes.get_all():
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {file.content_type}. "
                   f"Supported: {SupportedFileTypes.list()}"
        )
    
    try:
        result = await document_service.process_document(file)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
