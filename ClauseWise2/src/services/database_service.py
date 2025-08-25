import sqlite3
import os
from typing import List, Optional
from config.settings import settings
from src.models.feedback import FeedbackCreate, FeedbackInDB
from datetime import datetime

class DatabaseService:
    """Service for handling database operations"""
    
    def __init__(self):
        """Initialize the database service"""
        self.db_path = settings.DATABASE_URL.replace("sqlite:///", "")
        self.init_database()
    
    def init_database(self):
        """Initialize the database and create tables if they don't exist"""
        # Create directory if it doesn't exist
        db_dir = os.path.dirname(self.db_path)
        if db_dir and not os.path.exists(db_dir):
            os.makedirs(db_dir)
        
        # Create feedback table
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                document_id TEXT,
                clause_text TEXT,
                feedback_type TEXT NOT NULL,
                rating INTEGER NOT NULL,
                comment TEXT,
                user_id TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conn.commit()
        conn.close()
    
    def create_feedback(self, feedback: FeedbackCreate) -> FeedbackInDB:
        """Create a new feedback entry"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO feedback (
                document_id, clause_text, feedback_type, rating, comment, user_id, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            feedback.document_id,
            feedback.clause_text,
            feedback.feedback_type,
            feedback.rating,
            feedback.comment,
            feedback.user_id,
            datetime.now(),
            datetime.now()
        ))
        
        feedback_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return FeedbackInDB(
            id=feedback_id,
            document_id=feedback.document_id,
            clause_text=feedback.clause_text,
            feedback_type=feedback.feedback_type,
            rating=feedback.rating,
            comment=feedback.comment,
            user_id=feedback.user_id,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
    
    def get_feedback_by_id(self, feedback_id: int) -> Optional[FeedbackInDB]:
        """Get feedback by ID"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM feedback WHERE id = ?", (feedback_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return FeedbackInDB(
                id=row[0],
                document_id=row[1],
                clause_text=row[2],
                feedback_type=row[3],
                rating=row[4],
                comment=row[5],
                user_id=row[6],
                created_at=datetime.fromisoformat(row[7]),
                updated_at=datetime.fromisoformat(row[8])
            )
        
        return None
    
    def get_feedback_by_document(self, document_id: str) -> List[FeedbackInDB]:
        """Get all feedback for a document"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM feedback WHERE document_id = ?", (document_id,))
        rows = cursor.fetchall()
        conn.close()
        
        feedback_list = []
        for row in rows:
            feedback_list.append(FeedbackInDB(
                id=row[0],
                document_id=row[1],
                clause_text=row[2],
                feedback_type=row[3],
                rating=row[4],
                comment=row[5],
                user_id=row[6],
                created_at=datetime.fromisoformat(row[7]),
                updated_at=datetime.fromisoformat(row[8])
            ))
        
        return feedback_list
    
    def update_feedback(self, feedback_id: int, rating: Optional[int] = None, comment: Optional[str] = None) -> Optional[FeedbackInDB]:
        """Update feedback"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Build update query dynamically
        update_fields = []
        params = []
        
        if rating is not None:
            update_fields.append("rating = ?")
            params.append(rating)
        
        if comment is not None:
            update_fields.append("comment = ?")
            params.append(comment)
        
        if not update_fields:
            return self.get_feedback_by_id(feedback_id)
        
        update_fields.append("updated_at = ?")
        params.append(datetime.now())
        params.append(feedback_id)
        
        query = f"UPDATE feedback SET {', '.join(update_fields)} WHERE id = ?"
        cursor.execute(query, params)
        
        conn.commit()
        conn.close()
        
        return self.get_feedback_by_id(feedback_id)
    
    def delete_feedback(self, feedback_id: int) -> bool:
        """Delete feedback"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM feedback WHERE id = ?", (feedback_id,))
        rows_affected = cursor.rowcount
        
        conn.commit()
        conn.close()
        
        return rows_affected > 0