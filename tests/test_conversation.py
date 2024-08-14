import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_conversation():
    response = client.post(
        "/api/v1/conversation",
        json={"message": "Hello, how are you?"}
    )
    assert response.status_code == 200
    assert "id" in response.json()
    assert "response" in response.json()
    assert "audio_url" in response.json()

def test_get_conversation():
    # First, create a conversation
    create_response = client.post(
        "/api/v1/conversation",
        json={"message": "Test message"}
    )
    conversation_id = create_response.json()["id"]

    # Then, retrieve the conversation
    get_response = client.get(f"/api/v1/conversation/{conversation_id}")
    assert get_response.status_code == 200
    assert get_response.json()["id"] == conversation_id
    assert "user_message" in get_response.json()
    assert "ai_response" in get_response.json()