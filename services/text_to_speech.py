import os
import hashlib
import pyttsx3
from dotenv import load_dotenv
from http.server import SimpleHTTPRequestHandler, HTTPServer

load_dotenv()

class TextToSpeech:
    def __init__(self):
        self.service_enabled = os.getenv("SERVICE_ENABLED", "true").lower() == "true"
        if self.service_enabled:
            self.engine = pyttsx3.init()

    def convert(self, text):
        if not self.service_enabled:
            return None
        filename = f"audio_{hashlib.md5(text.encode()).hexdigest()}.mp3"
        output_file = os.path.join("audio_files", filename)
        os.makedirs("audio_files", exist_ok=True)
        self.engine.save_to_file(text, output_file)
        self.engine.runAndWait()
        return f"http://localhost:7000/{filename}"

    def start_server(self):
        os.chdir("audio_files")
        httpd = HTTPServer(('localhost', 7000), SimpleHTTPRequestHandler)
        httpd.serve_forever()

text_to_speech = TextToSpeech()