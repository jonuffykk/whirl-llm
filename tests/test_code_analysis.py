import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_analyze_code():
    code = "def hello_world():\n    print('Hello, World!')"
    response = client.post(
        "/api/v1/code/analyze",
        json={"code": code}
    )
    assert response.status_code == 200
    assert "analysis" in response.json()

def test_generate_code():
    description = "Create a function that calculates the factorial of a number"
    response = client.post(
        "/api/v1/code/generate",
        json={"description": description}
    )
    assert response.status_code == 200
    assert "def factorial" in response.json()

def test_execute_code():
    code = "print('Hello, World!')"
    response = client.post(
        "/api/v1/code/execute",
        json={"code": code, "language": "python"}
    )
    assert response.status_code == 200
    assert response.json()["output"] == "Hello, World!\n"
    assert response.json()["error"] == ""
    assert response.json()["return_code"] == 0