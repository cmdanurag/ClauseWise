import asyncio
from typing import Dict, Any
from config.settings import settings
from google import genai
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AIService:
    """Service for interacting with Google GenAI (Vertex AI successor) for legal document analysis"""

    def __init__(self):
        """Initialize the AI service with Google GenAI credentials"""
        try:
            # Initialize GenAI client with API key
            self.client = genai.Client(api_key=settings.GOOGLE_API_KEY)

            logger.info("AI Service (google-genai) initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize AI Service: {str(e)}")
            raise

    async def analyze_document(self, document_text: str, document_type: str) -> Dict[str, Any]:
        """Analyze a legal document and provide comprehensive analysis"""
        try:
            prompt = self._create_document_analysis_prompt(document_text, document_type)

            response = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: self.client.models.generate_content(
                    model=settings.AIPLATFORM_MODEL_NAME,
                    contents=prompt
                )
            )

            return self._parse_document_analysis_response(response.text)
        except Exception as e:
            logger.error(f"Document analysis failed: {str(e)}")
            raise Exception(f"Failed to analyze document: {str(e)}")

    async def explain_clause(self, clause_text: str, context: str = "") -> Dict[str, Any]:
        """Explain a specific clause in plain language"""
        try:
            prompt = self._create_clause_explanation_prompt(clause_text, context)

            response = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: self.client.models.generate_content(
                    model=settings.AIPLATFORM_MODEL_NAME,
                    contents=prompt
                )
            )

            return self._parse_clause_explanation_response(response.text)
        except Exception as e:
            logger.error(f"Clause explanation failed: {str(e)}")
            raise Exception(f"Failed to explain clause: {str(e)}")

    async def assess_risk(self, clause_text: str, document_type: str) -> Dict[str, Any]:
        """Assess the risk level of a specific clause"""
        try:
            prompt = self._create_risk_assessment_prompt(clause_text, document_type)

            response = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: self.client.models.generate_content(
                    model=settings.AIPLATFORM_MODEL_NAME,
                    contents=prompt
                )
            )

            return self._parse_risk_assessment_response(response.text)
        except Exception as e:
            logger.error(f"Risk assessment failed: {str(e)}")
            raise Exception(f"Failed to assess risk: {str(e)}")

    async def answer_question(self, question: str, document_context: str) -> Dict[str, Any]:
        """Answer a user question about a document"""
        try:
            prompt = self._create_question_answering_prompt(question, document_context)

            response = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: self.client.models.generate_content(
                    model=settings.AIPLATFORM_MODEL_NAME,
                    contents=prompt
                )
            )

            return self._parse_question_answering_response(response.text)
        except Exception as e:
            logger.error(f"Question answering failed: {str(e)}")
            raise Exception(f"Failed to answer question: {str(e)}")

    # ---------------------
    # Prompt Builders
    # ---------------------

    def _create_document_analysis_prompt(self, document_text: str, document_type: str) -> str:
        return f"""
        Analyze the following {document_type} and provide a comprehensive analysis:

        Document Text:
        {document_text}

        Please provide:
        1. A brief summary of the document (2-3 sentences)
        2. A list of key clauses with explanations in plain language
        3. Risk assessment for each clause (low, medium, high)
        4. Recommendations for negotiation or modification
        5. Potential issues to be aware of

        Format your response as a structured analysis.
        """

    def _create_clause_explanation_prompt(self, clause_text: str, context: str = "") -> str:
        prompt = f"""
        Explain the following legal clause in plain, easy-to-understand language:

        Clause:
        {clause_text}
        """
        if context:
            prompt += f"\nContext:\n{context}"

        prompt += """
        
        Please provide:
        1. A plain language explanation of what this clause means
        2. Why it's important
        3. Potential implications for the reader
        4. Any risks associated with this clause

        Format your response clearly and concisely.
        """
        return prompt

    def _create_risk_assessment_prompt(self, clause_text: str, document_type: str) -> str:
        return f"""
        Assess the risk level of the following clause from a {document_type}:

        Clause:
        {clause_text}

        Please provide:
        1. Risk level (low, medium, high)
        2. Explanation of why this risk level was assigned
        3. Potential consequences if this clause is enforced
        4. Recommendations for addressing this risk

        Be specific and provide actionable advice.
        """

    def _create_question_answering_prompt(self, question: str, document_context: str) -> str:
        return f"""
        Answer the following question about a legal document:

        Question:
        {question}

        Document Context:
        {document_context}

        Please provide:
        1. A clear, direct answer to the question
        2. Supporting information from the document context
        3. Any relevant caveats or considerations
        4. Additional recommendations if applicable

        Keep your answer focused and practical.
        """

    # ---------------------
    # Response Parsers
    # ---------------------

    def _parse_document_analysis_response(self, response_text: str) -> Dict[str, Any]:
        return {"analysis": response_text, "status": "success"}

    def _parse_clause_explanation_response(self, response_text: str) -> Dict[str, Any]:
        return {"explanation": response_text, "status": "success"}

    def _parse_risk_assessment_response(self, response_text: str) -> Dict[str, Any]:
        return {"risk_assessment": response_text, "status": "success"}

    def _parse_question_answering_response(self, response_text: str) -> Dict[str, Any]:
        return {"answer": response_text, "status": "success"}
