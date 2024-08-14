from services.file_handler import FileHandler
from services.llm_engine import llm_engine

class DocumentProcessor:
    def __init__(self):
        self.file_handler = FileHandler()

    async def analyze(self, file):
        content = await self.file_handler.read_file(file)
        return await llm_engine.generate_response(f"Analyze the following document:\n\n{content}")

    async def summarize(self, file):
        content = await self.file_handler.read_file(file)
        return await llm_engine.summarize_document(content)

    async def extract_text(self, file):
        return await self.file_handler.read_file(file)