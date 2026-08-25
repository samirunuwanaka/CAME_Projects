"""
Unit tests for FastAPI sub-agent API endpoints and static routes.
"""

from fastapi.testclient import TestClient
from app.fast_api_app import app

client = TestClient(app)


def test_serve_index_route() -> None:
    response = client.get("/dashboard")
    assert response.status_code == 200
    assert "AeroTrip AI" in response.text


def test_api_plan_endpoint() -> None:
    payload = {
        "origin": "SFO",
        "destination": "Tokyo",
        "duration_days": 5,
        "budget": 3500.0,
        "travel_purpose": "Client Meetings",
        "preferences": "Gym, Vegetarian meals",
        "passport_valid_months": 8,
        "visa_status": "Approved"
    }
    response = client.post("/api/plan", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert "flight_planner_agent" in str(data["sub_agents_executed"])
    assert "places_explorer_agent" in str(data["sub_agents_executed"])
    assert "PASSED" in data["guardrail_report"]
    assert "Places to Visit in Tokyo" in data["places_to_visit"]
    assert "Flight Suggestions: SFO to Tokyo" in data["flight_suggestions"]


def test_api_guardrails_endpoint() -> None:
    payload = {
        "origin": "NYC",
        "destination": "NYC",
        "total_budget": 1000.0,
        "duration_days": 3
    }
    response = client.post("/api/guardrails", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "BLOCKED" in data["guardrail_report"]


def test_api_flights_endpoint() -> None:
    response = client.post("/api/flights?origin=SFO&destination=NYC&duration_days=4")
    assert response.status_code == 200
    data = response.json()
    assert data["sub_agent"] == "flight_planner_agent"
    assert "Flight Suggestions" in data["flights"]


def test_api_places_endpoint() -> None:
    response = client.post("/api/places?destination=Paris&purpose=Tourism&duration_days=3")
    assert response.status_code == 200
    data = response.json()
    assert data["sub_agent"] == "places_explorer_agent"
    assert "Places to Visit in Paris" in data["places"]
