from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

# Load API Key Securely
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY is not set in the environment variables.")

genai.configure(api_key=GEMINI_API_KEY)

class QuestionRequest(BaseModel):
    experience: str
    job_role: str
    company: str

@router.post("/generate")
async def generate_questions(request: QuestionRequest):
    """
    Generates AI-powered interview questions based on job role, company, and experience level.
    """
    try:
        prompt = f"""
        Generate exactly 5 interview questions for a {request.job_role} position at {request.company} 
        for a candidate with {request.experience} experience.
        
        Format them in a numbered list.
        """
        model = genai.GenerativeModel('gemini-pro')

        # Use the appropriate method to generate content from Gemini API
        response = model.generate_text(prompt=prompt)

        if not response or not response.text:
            return {"questions": ["❌ No questions generated. Please try again."]}

        # Split based on numbered list output
        questions = [q.strip() for q in response.text.split("\n") if q.strip()]

        return {"questions": questions[:5]}  # Ensure exactly 5 questions

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating questions: {str(e)}")
