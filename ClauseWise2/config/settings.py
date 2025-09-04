from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Application settings
    APP_NAME: str = "ClauseWise"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    
    # Google GenAI / Vertex AI settings
    GOOGLE_API_KEY: str  # required for google-genai
    AIPLATFORM_MODEL_NAME: str = "gemini-1.5-pro"  # default GenAI model
    GCP_PROJECT_ID: str ="clausewise-469615" # required for Vertex AI
    GCP_REGION: str = "us-central1"  # default region
    VERTEX_AI_ENDPOINT_ID: str  # deployed Vertex AI endpoint ID

    # Storage settings
    GCS_BUCKET_NAME: Optional[str] = None
    MAX_FILE_SIZE_MB: int = 10
    
    # Database settings
    DATABASE_URL: str = "sqlite:///./clausewise.db"
    
    # Security settings
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Rate limiting settings
    RATE_LIMIT_REQUESTS: int = 100
    RATE_LIMIT_WINDOW: int = 3600
    
    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
