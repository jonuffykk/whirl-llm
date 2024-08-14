from fastapi import APIRouter, Depends, UploadFile, File
from services.llm_engine import llm_engine
from models.conversation import Conversation
from core.database import get_db
from services.text_to_speech import text_to_speech

router = APIRouter()

@router.post("/")
async def create_conversation(message: str, db = Depends(get_db)):
    response = await llm_engine.generate_response(message)
    audio_file = text_to_speech.convert(response)
    conversation = Conversation(user_message=message, ai_response=response, audio_file=audio_file)
    result = await db.conversations.insert_one(conversation.dict())
    return {"id": str(result.inserted_id), "response": response, "audio_url": audio_file}

@router.get("/{conversation_id}")
async def get_conversation(conversation_id: str, db = Depends(get_db)):
    conversation = await db.conversations.find_one({"_id": conversation_id})
    return conversation

@router.post("/analyze_document")
async def analyze_document(file: UploadFile = File(...)):
    contents = await file.read()
    with open(file.filename, "wb") as f:
        f.write(contents)
    
    summary = await llm_engine.summarize_document(file.filename)
    return {"summary": summary}

@router.post("/generate_file_editor")
async def generate_file_editor(file_type: str, operation: str):
    code = await llm_engine.generate_file_editor(file_type, operation)
    return {"code": code}