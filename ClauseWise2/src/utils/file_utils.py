import os
from fastapi import UploadFile, HTTPException
from typing import List
from src.utils.constants import SupportedFileTypes, MAX_FILE_SIZE_MB, ALLOWED_EXTENSIONS

def validate_file(file: UploadFile) -> None:
    """Validate uploaded file"""
    
    # Check file size
    if hasattr(file, 'size') and file.size:
        if file.size > MAX_FILE_SIZE_MB * 1024 * 1024:
            raise HTTPException(
                status_code=413,
                detail=f"File too large. Maximum size is {MAX_FILE_SIZE_MB}MB"
            )
    
    # Check file extension
    if file.filename:
        _, ext = os.path.splitext(file.filename.lower())
        if ext not in ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=400,
                detail=f"Unsupported file type. Allowed: {', '.join(ALLOWED_EXTENSIONS)}"
            )
    
    # Check MIME type
    if file.content_type not in SupportedFileTypes.get_all():
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported content type: {file.content_type}"
        )

def get_file_extension(filename: str) -> str:
    """Get file extension"""
    return os.path.splitext(filename.lower())[1]