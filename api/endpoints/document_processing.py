from fastapi import APIRouter, UploadFile, File, Depends
from services.document_processor import DocumentProcessor
from core.database import get_db
from models.document import Document

router = APIRouter()
document_processor = DocumentProcessor()

@router.post("/analyze")
async def analyze_document(file: UploadFile = File(...), db = Depends(get_db)):
    analysis = await document_processor.analyze(file)
    document = Document(filename=file.filename, analysis=analysis)
    result = await db.documents.insert_one(document.dict())
    return {"id": str(result.inserted_id), "analysis": analysis}

@router.post("/summarize")
async def summarize_document(file: UploadFile = File(...)):
    return await document_processor.summarize(file)

@router.post("/extract_text")
async def extract_text(file: UploadFile = File(...)):
    return await document_processor.extract_text(file)