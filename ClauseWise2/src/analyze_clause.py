import os
from google import genai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get project and region from .env
PROJECT_ID = os.getenv("PROJECT_ID")
REGION = os.getenv("REGION")
MODEL = os.getenv("AIPLATFORM_MODEL_NAME", "gemini-2.5-flash")

# Validate required environment variables
if not PROJECT_ID or not REGION:
    raise ValueError("PROJECT_ID and REGION must be set in the .env file.")

# Initialize the Gen AI client (Vertex AI)
client = genai.Client(
    vertexai=True,
    project=str(PROJECT_ID),
    location=str(REGION)
)

def analyze_clause(clause_text: str) -> str:
    """
    Sends a single clause to Gemini for risk analysis.
    Returns the model's response as a string.
    """
    if not clause_text.strip():
        return "No text provided for analysis."

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=f"Analyze the risk of this clause:\n{clause_text}"
        )
        return response.text
    except Exception as e:
        return f"Error analyzing clause: {e}"

# Example usage for testing
if __name__ == "__main__":
    test_clause = "The tenant must pay rent by the 5th of every month."
    print(analyze_clause(test_clause))
