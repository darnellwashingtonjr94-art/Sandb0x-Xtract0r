import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router as api_router

app = FastAPI(
    title="S@ndb0x-Xtract0r API",
    description="REST API gateway for automated cross-platform sandbox analysis and multi-LLM reporting.",
    version="1.0.0"
)

# Enable CORS for web UI integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "healthy", "engine": "S@ndb0x-Xtract0r", "version": "1.0.0"}
