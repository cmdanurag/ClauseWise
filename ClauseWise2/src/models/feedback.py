from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FeedbackBase(BaseModel):
    """Base model for feedback"""
    document_id: Optional[str] = None
    clause_text: Optional[str] = None
    feedback_type: str  # "document_analysis", "clause_explanation", "risk_assessment", "question_answer"
    rating: int  # 1-5 star rating
    comment: Optional[str] = None
    user_id: Optional[str] = None

class FeedbackCreate(FeedbackBase):
    """Model for creating feedback"""
    pass

class FeedbackUpdate(BaseModel):
    """Model for updating feedback"""
    rating: Optional[int] = None
    comment: Optional[str] = None

class FeedbackInDB(FeedbackBase):
    """Model for feedback stored in database"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True