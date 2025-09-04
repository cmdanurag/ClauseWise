from fastapi import APIRouter, HTTPException, UploadFile, File
from src.models.document_models import DocumentUploadRequest, DocumentAnalysisResponse
from src.services.vertex_ai_service import analyze_document

router = APIRouter()

@router.post(
    "/documents/upload",
    response_model=DocumentAnalysisResponse
)
async def upload_document(data: DocumentUploadRequest):
    try:
        analysis_result = analyze_document(data.content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return DocumentAnalysisResponse(status="success", analysis=analysis_result)


@router.post(
    "/documents/upload-file",
    response_model=DocumentAnalysisResponse
)
async def upload_document_file(file: UploadFile = File(...)):
    try:
        content = await file.read()
        text = content.decode("utf-8")  # For PDFs, use a PDF parser instead
        analysis_result = analyze_document(text)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to process file: {str(e)}")

    return DocumentAnalysisResponse(status="success", analysis=analysis_result)
