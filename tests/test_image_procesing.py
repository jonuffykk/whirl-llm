import pytest
from fastapi.testclient import TestClient
from main import app
import io
from PIL import Image

client = TestClient(app)

def create_test_image():
    file = io.BytesIO()
    image = Image.new('RGB', size=(100, 100), color=(255, 0, 0))
    image.save(file, 'png')
    file.name = 'test.png'
    file.seek(0)
    return file

def test_analyze_image():
    test_image = create_test_image()
    response = client.post(
        "/api/v1/image/analyze",
        files={"file": ("test.png", test_image, "image/png")}
    )
    assert response.status_code == 200
    assert "top_classes" in response.json()
    assert "probabilities" in response.json()