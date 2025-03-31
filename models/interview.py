from .database import get_db_connection

# Function to create interview session
def create_interview_session(user_id, job_role, experience_level, company):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO interview_sessions (user_id, job_role, experience_level, company, created_at) 
            VALUES (%s, %s, %s, %s, NOW())
            """
            cursor.execute(sql, (user_id, job_role, experience_level, company))
            connection.commit()
            return cursor.lastrowid  # Returns the inserted interview session ID
    finally:
        connection.close()
