from fastapi import APIRouter, HTTPException, Body
from typing import List
from src.services import DatabaseService
from src.models.feedback import FeedbackCreate, FeedbackInDB, FeedbackUpdate

router = APIRouter(prefix="/feedback", tags=["feedback"])
db_service = DatabaseService()

@router.post("/", response_model=FeedbackInDB)
async def create_feedback(feedback: FeedbackCreate):
    """
    Create a new feedback entry
    
    Args:
        feedback: Feedback data to create
        
    Returns:
        Created feedback entry
    """
    try:
        created_feedback = db_service.create_feedback(feedback)
        return created_feedback
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create feedback: {str(e)}")

@router.get("/{feedback_id}", response_model=FeedbackInDB)
async def get_feedback(feedback_id: int):
    """
    Get feedback by ID
    
    Args:
        feedback_id: ID of the feedback to retrieve
        
    Returns:
        Feedback entry
    """
    try:
        feedback = db_service.get_feedback_by_id(feedback_id)
        if not feedback:
            raise HTTPException(status_code=404, detail="Feedback not found")
        return feedback
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get feedback: {str(e)}")

@router.get("/document/{document_id}", response_model=List[FeedbackInDB])
async def get_feedback_by_document(document_id: str):
    """
    Get all feedback for a document
    
    Args:
        document_id: ID of the document to get feedback for
        
    Returns:
        List of feedback entries
    """
    try:
        feedback_list = db_service.get_feedback_by_document(document_id)
        return feedback_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get feedback: {str(e)}")

@router.put("/{feedback_id}", response_model=FeedbackInDB)
async def update_feedback(
    feedback_id: int,
    rating: int = Body(None),
    comment: str = Body(None)
):
    """
    Update feedback
    
    Args:
        feedback_id: ID of the feedback to update
        rating: New rating (optional)
        comment: New comment (optional)
        
    Returns:
        Updated feedback entry
    """
    try:
        updated_feedback = db_service.update_feedback(feedback_id, rating, comment)
        if not updated_feedback:
            raise HTTPException(status_code=404, detail="Feedback not found")
        return updated_feedback
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update feedback: {str(e)}")

@router.delete("/{feedback_id}")
async def delete_feedback(feedback_id: int):
    """
    Delete feedback
    
    Args:
        feedback_id: ID of the feedback to delete
        
    Returns:
        Success message
    """
    try:
        deleted = db_service.delete_feedback(feedback_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Feedback not found")
        return {"message": "Feedback deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete feedback: {str(e)}")