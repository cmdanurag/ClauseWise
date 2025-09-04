# backend/app/api/routes/ai_routes.py
from fastapi import APIRouter
from pydantic import BaseModel
from google.cloud import aiplatform

router = APIRouter()

# Request schema
class DocumentText(BaseModel):
    text: str

# Initialize Vertex AI
aiplatform.init(project="YOUR_GCP_PROJECT_ID", location="us-central1")

# Replace with your Vertex AI model ID
MODEL_ID = "YOUR_MODEL_ID"
model = aiplatform.TextGenerationModel(model_name=MODEL_ID)

@router.post("/analyze")
def analyze_document(doc: DocumentText):
    """
    Accepts document text and returns AI-generated analysis.
    """
    response = model.predict(
        doc.text,
        max_output_tokens=500,
        temperature=0.2
    )
    return {"status": "success", "analysis": response.text}
