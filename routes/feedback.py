from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load API Key for Gemini
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY is not set in the environment variables.")

genai.configure(api_key=GEMINI_API_KEY)

router = APIRouter()

# Request Model
class ResponseInput(BaseModel):
    question: str
    user_answer: str

@router.post("/evaluate")
def evaluate_response(input_data: ResponseInput):

    """AI-powered feedback system analyzing the candidate's response."""
    
    prompt = f"""
    You are an expert technical interviewer. Evaluate the candidate's response to the given question.

    **Question:** {input_data.question}
    **Candidate's Answer:** {input_data.user_answer}

    Provide a structured evaluation:
    - Strengths of the answer
    - Weaknesses or areas of improvement
    - Overall rating (out of 10)
    """

    try:
        # Using the correct API method to generate content
        model = genai.GenerativeModel('gemini-pro')

        response = model.generate_text(prompt=prompt)

        # Ensure response is valid
        feedback = response.strip() if response else "No feedback generated."

        return {"feedback": feedback}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating feedback: {str(e)}")
