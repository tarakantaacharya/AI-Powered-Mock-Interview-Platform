from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models.database import get_db_connection
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

class PerformanceRequest(BaseModel):
    user_id: int
    interview_id: int
    score: float
    feedback: str

@router.post("/track")
async def track_performance(request: PerformanceRequest):
    """
    Stores interview performance in the database.
    """
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO interview_performance (user_id, interview_id, score, feedback) 
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (request.user_id, request.interview_id, request.score, request.feedback))
            connection.commit()  # Commit the transaction
            return {"message": "✅ Performance tracked successfully!"}
    
    except Exception as e:
        # In case of error, return an HTTPException with the error message
        raise HTTPException(status_code=500, detail=f"❌ Error tracking performance: {str(e)}")
    
    finally:
        # Ensure the connection is always closed
        connection.close()
