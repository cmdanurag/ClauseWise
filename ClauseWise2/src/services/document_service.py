from src.services.text_extraction_service import TextExtractionService
from src.services.ai_service import AIService

class DocumentService:
    def __init__(self):
        self.text_extractor = TextExtractionService()
        self.ai = AIService()  # Can swap later with LangChain
    
    def get_supported_formats(self):
        return ["pdf", "docx", "txt"]

    async def process_document(self, file):
        # Step 1: Extract text
        text = await self.text_extractor.extract_text(file)

        # Step 2: Analyze with AI
        analysis = self.ai.analyze(text)

        # Step 3: Return structured response
        return {
            "filename": file.filename,
            "analysis": analysis
        }
