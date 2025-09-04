from google.cloud import aiplatform

# Replace with your project info
PROJECT_ID = "your-gcp-project-id"
REGION = "us-central1"

def main():
    aiplatform.init(project=PROJECT_ID, location=REGION)
    print("Vertex AI initialized successfully!")

if __name__ == "__main__":
    main()
