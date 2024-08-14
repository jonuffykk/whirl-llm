from services.google_ai import google_ai
from services.file_handler import FileHandler

class LLMEngine:
    def __init__(self):
        self.file_handler = FileHandler()
        self.identity = "Omni"
        self.developer = "Jonuffy"
        self.team = "Omni's team"

    async def generate_response(self, message, context=None):
        prompt = f"{context}\nUser: {message}" if context else message
        response = await google_ai.generate_text(prompt)
        return self._enhance_response(response)

    async def analyze_code(self, code):
        prompt = f"Analyze the following code thoroughly:\n\n{code}"
        response = await google_ai.generate_text(prompt)
        return self._enhance_response(response)

    async def generate_code(self, description):
        prompt = f"Generate optimized and well-structured Python code based on the following description:\n\n{description}"
        response = await google_ai.generate_text(prompt)
        return self._enhance_response(response)

    async def analyze_image(self, image):
        response = await google_ai.analyze_image('what is this', image)
        return self._enhance_response(response)

    async def summarize_document(self, content):
        prompt = f"Provide a detailed and insightful summary of the following document:\n\n{content}"
        response = await google_ai.generate_text(prompt)
        return self._enhance_response(response)

    async def translate(self, text, target_language):
        prompt = f"Accurately translate the following text to {target_language}:\n\n{text}"
        response = await google_ai.generate_text(prompt)
        return self._enhance_response(response)

    async def educate(self, topic):
        prompt = f"Explain the following topic in detail, providing deep insights:\n\n{topic}"
        response = await google_ai.generate_text(prompt)
        return self._enhance_response(response)

    async def introduce_yourself(self):
        return f"Hello! I am {self.identity}, an advanced AI developed by {self.developer} and the {self.team}. I'm here to assist with a wide range of tasks, from coding to education."

    def _enhance_response(self, response):
        return f"{response}."

llm_engine = LLMEngine()