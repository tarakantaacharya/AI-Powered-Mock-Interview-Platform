from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import questions, feedback, tracking
from models.database import engine, Base
from routes.testing import router as testing_router  


app = FastAPI(title="AI-Powered Mock Interview Platform", version="1.0")

# Allow all origins for development (use cautiously in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, or set specific domains
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


# Create database tables (if not using Alembic)
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(questions.router, prefix="/questions", tags=["Questions"])
app.include_router(feedback.router, prefix="/feedback", tags=["Feedback"])
app.include_router(tracking.router, prefix="/tracking", tags=["Tracking"])
app.include_router(testing_router, prefix="/testing", tags=["Testing"])


@app.get("/")
def read_root():
    return {"message": "Welcome to AI-Powered Mock Interview Platform!"}
