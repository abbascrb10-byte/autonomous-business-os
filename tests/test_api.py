import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    res = client.get("/api/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_workflow_route():
    payload = {
        "source": "requests",
        "source_id": "api_test_1",
        "raw_text": "I need to buy a MacBook Pro under $2500 shipped to US",
        "author_reference": "user_api"
    }
    res = client.post("/api/workflow/run?user_response=yes", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "COMMERCIAL_OFFER_SENT"
    assert data["offer_message"] is not None
    assert "affiliate" in data["offer_message"]["body"].lower() or "http" in data["offer_message"]["body"]
