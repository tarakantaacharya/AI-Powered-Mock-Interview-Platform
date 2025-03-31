from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

router = APIRouter()

# Initialize Gemini API
genai.configure(api_key="YOUR_GEMINI_API_KEY")

class QuestionRequest(BaseModel):
    experience: str
    job_role: str
    company: str

@router.post("/generate")
async def generate_questions(request: QuestionRequest):
    try:
        prompt = f"Generate 5 interview questions for a {request.job_role} at {request.company} with {request.experience} experience."
        response = genai.chat(prompt)
        
        return {"questions": response.text.split("\n")}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
