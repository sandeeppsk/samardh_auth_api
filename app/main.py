from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, users
from app.db.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

# Customize the API documentation
app = FastAPI(
    title="Samardh Authentication API",  # Changes the main title
    description="A comprehensive authentication and user management API",
    version="1.0.0",
    docs_url="/docs",  # Default swagger UI path
    redoc_url="/redoc"  # Default ReDoc path
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["authentication"])
app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Authentication & Authorization API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}