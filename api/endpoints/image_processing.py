from fastapi import APIRouter, UploadFile, File
from services.llm_engine import llm_engine

router = APIRouter()

@router.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    contents = await file.read()
    with open(file.filename, "wb") as f:
        f.write(contents)
    
    analysis = await llm_engine.analyze_image(file.filename)
    return {"analysis": analysis}