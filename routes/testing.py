from fastapi import APIRouter, HTTPException
from models.database import get_db_connection
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/sessions")
async def get_interview_sessions():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM interview_sessions"
            cursor.execute(sql)
            result = cursor.fetchall()  # Fetch all rows from the query
            
            # Ensure we have rows and process them
            if not result:
                return {"message": "No interview sessions found."}
            
            sessions = [{"id": row['id'], "user_id": row['user_id'], "job_role": row['job_role'],
                         "experience_level": row['experience_level'], "company": row['company'],
                         "created_at": row['created_at'].strftime('%Y-%m-%d %H:%M:%S')} for row in result]
            
            # Log the sessions to confirm the data
            print("Fetched interview sessions:", sessions)
            
            return JSONResponse(content={"sessions": sessions})
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving interview sessions: {str(e)}")
    
    finally:
        connection.close()
