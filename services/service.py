import os
import google.generativeai as genai

# Load API key from .env file
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load API key
GENAI_API_KEY = os.getenv("GENAI_API_KEY")
if not GENAI_API_KEY:
    raise ValueError("❌ GENAI_API_KEY is not set in the environment variables.")

# Configure Gemini AI
genai.configure(api_key=GENAI_API_KEY)

# Generate interview questions based on job role & experience
def generate_interview_questions(job_role: str, experience_level: str):
    prompt = f"Generate 5 technical interview questions for a {experience_level} {job_role}."
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text if response else "Failed to generate questions."

# Analyze interview response and provide AI feedback
def analyze_response(user_response: str, job_role: str):
    prompt = f"Evaluate this interview answer for a {job_role} role. Provide strengths, weaknesses, and suggestions for improvement.\n\nAnswer: {user_response}"
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text if response else "Failed to analyze response."
