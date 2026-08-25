"""
Unit tests for sub-agents, places to visit tools, prerequisites, and travel guardrails.
"""

from app.agent import (
    check_flight_prerequisites,
    search_places_to_visit,
    recommend_local_dining,
    validate_travel_guardrails,
    ask_prerequisites_checklist,
    flight_planner_agent,
    places_explorer_agent,
    root_agent,
)


def test_check_flight_prerequisites() -> None:
    result = check_flight_prerequisites("SFO", "NYC", 8, "Valid Visa")
    assert "Flight & Travel Prerequisites Check" in result
    assert "Passport Validity" in result
    assert "8 months remaining" in result
    assert "Valid Visa" in result


def test_search_places_to_visit() -> None:
    result = search_places_to_visit("Paris", "business", "museums", 4)
    assert "Places to Visit in Paris" in result
    assert "Places Explorer Sub-Agent" in result
    assert "Highlights" in result


def test_recommend_local_dining() -> None:
    result = recommend_local_dining("Tokyo", "seafood")
    assert "Local Dining & Culinary Spots in Tokyo" in result
    assert "Atmosphere" in result


def test_validate_travel_guardrails_pass() -> None:
    result = validate_travel_guardrails("SFO", "NYC", 2500.0, 5)
    assert "Travel Guardrails Evaluation Report" in result
    assert "PASSED" in result


def test_validate_travel_guardrails_block_same_origin_dest() -> None:
    result = validate_travel_guardrails("SFO", "SFO", 2500.0, 5)
    assert "BLOCKED" in result
    assert "Origin and Destination cannot be the exact same location" in result


def test_ask_prerequisites_checklist() -> None:
    result = ask_prerequisites_checklist("London")
    assert "Required Travel Prerequisites Checklist for London" in result
    assert "Passport Expiry Date" in result
    assert "Travel Insurance" in result


def test_subagent_structures() -> None:
    assert flight_planner_agent.name == "flight_planner_agent"
    assert places_explorer_agent.name == "places_explorer_agent"
    assert len(root_agent.sub_agents) == 2
    sub_names = [agent.name for agent in root_agent.sub_agents]
    assert "flight_planner_agent" in sub_names
    assert "places_explorer_agent" in sub_names
