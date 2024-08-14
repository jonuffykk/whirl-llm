from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints import conversation, code_analysis, image_processing, document_processing
from core.config import settings
from core.database import init_db, close_db_connection
from utils.logger import setup_logging

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(conversation.router, prefix=settings.API_V1_STR + "/conversation", tags=["conversation"])
app.include_router(code_analysis.router, prefix=settings.API_V1_STR + "/code", tags=["code"])
app.include_router(image_processing.router, prefix=settings.API_V1_STR + "/image", tags=["image"])
app.include_router(document_processing.router, prefix=settings.API_V1_STR + "/document", tags=["document"])

@app.on_event("startup")
async def startup_event():
    await init_db()
    setup_logging()

@app.on_event("shutdown")
async def shutdown_event():
    await close_db_connection()

@app.get("/", tags=["health"])
async def root():
    return {"status": "healthy", "version": settings.APP_VERSION}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)