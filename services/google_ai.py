import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

class OmniLLM:
    def __init__(self):
        self._initialize_models()

    def _initialize_models(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key=api_key)
        self.text_model = genai.GenerativeModel('gemini-pro')
        self.image_model = genai.GenerativeModel('gemini-pro')

    async def generate_text(self, prompt):
        try:
            response = await self.text_model.generate_content_async(prompt)
            return self._sanitize_response(response.text)
        except Exception as e:
            return self._handle_error(f"Text generation error: {str(e)}")

    async def analyze_image(self, image_path, prompt):
        try:
            image = genai.types.Image.from_file(image_path)
            response = await self.image_model.generate_content_async([prompt, image])
            return self._sanitize_response(response.text)
        except Exception as e:
            return self._handle_error(f"Image analysis error: {str(e)}")

    def _sanitize_response(self, response_text):
        return response_text.strip()

    def _handle_error(self, message):
        return f"Omni LLM encountered an issue: {message}"

google_ai = OmniLLM()