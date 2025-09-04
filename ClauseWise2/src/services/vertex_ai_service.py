# src/services/vertex_ai_service.py

import os
from google.cloud import aiplatform
from google.cloud.aiplatform.gapic.schema import predict
from config.settings import settings

# Initialize Vertex AI
def init_vertex_ai():
    """
    Initialize Vertex AI with project and region from settings.
    """
    aiplatform.init(
        project=os.getenv("GOOGLE_CLOUD_PROJECT", settings.GOOGLE_CLOUD_PROJECT),
        location=os.getenv("AIPLATFORM_LOCATION", settings.AIPLATFORM_LOCATION),
    )
    print("Vertex AI initialized successfully!")

# Call this on import
init_vertex_ai()


def analyze_document(text: str) -> str:
    """
    Send the document text to the Vertex AI endpoint for analysis.
    Returns AI-generated analysis as string.
    """
    endpoint_id = os.getenv("AIPLATFORM_ENDPOINT_ID")
    if not endpoint_id:
        raise ValueError("AIPLATFORM_ENDPOINT_ID not set in .env")

    # Create endpoint object
    endpoint = aiplatform.Endpoint(endpoint_id)

    # Call prediction
    response = endpoint.predict(
        instances=[{"content": text}],
        parameters={}  # You can customize parameters if needed
    )

    # Extract predictions (depends on your model)
    # For GenAI / text models, usually a single string in predictions[0]['content']
    predictions = response.predictions
    if not predictions:
        return "No analysis returned"
    
    # If using structured responses, adjust accordingly
    return predictions[0].get("content", str(predictions[0]))
