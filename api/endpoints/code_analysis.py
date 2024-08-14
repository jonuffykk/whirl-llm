from fastapi import APIRouter, Depends, HTTPException
from services.llm_engine import llm_engine
from services.code_executor import CodeExecutor
from models.project import Project
from core.database import get_db

router = APIRouter()
code_executor = CodeExecutor()

@router.post("/analyze")
async def analyze_code(code: str, db = Depends(get_db)):
    analysis = await llm_engine.analyze_code(code)
    project = Project(code=code, analysis=analysis)
    await db.projects.insert_one(project.dict())
    return analysis

@router.post("/generate")
async def generate_code(description: str):
    return await llm_engine.generate_code(description)

@router.post("/execute")
async def execute_code(code: str, language: str):
    try:
        if language.lower() == "python":
            return await code_executor.execute_python(code)
        elif language.lower() == "javascript":
            return await code_executor.execute_javascript(code)
        else:
            raise HTTPException(status_code=400, detail="Unsupported language")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))