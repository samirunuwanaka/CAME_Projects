# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Unit tests for the travel-planning tools.
"""

from app.agent import (
    search_flights,
    recommend_hotels,
    generate_business_itinerary,
    estimate_budget_breakdown,
)


def test_search_flights() -> None:
    """Test flight search tool logic and output format."""
    result = search_flights("SFO", "NYC", 5)
    assert "Flight Suggestions" in result
    assert "SFO to NYC" in result
    assert "Economy" in result
    assert "Business" in result


def test_recommend_hotels() -> None:
    """Test hotel recommendations tool logic and output format."""
    result = recommend_hotels("New York", 2000.0, 5, "near financial district")
    assert "Hotel/Stay Recommendations in New York" in result
    assert "near financial district" in result


def test_generate_business_itinerary() -> None:
    """Test business itinerary generation tool logic and output format."""
    result = generate_business_itinerary("Chicago", 3, "partnership talks", "vegetarian meals")
    assert "Day-by-Day Business Itinerary: Chicago" in result
    assert "partnership talks" in result
    assert "Day 1:" in result
    assert "Day 2:" in result
    assert "Day 3:" in result
    assert "vegetarian meals" in result


def test_estimate_budget_breakdown() -> None:
    """Test budget estimation tool logic and output format."""
    result = estimate_budget_breakdown("SFO", "NYC", 4, 1500.0)
    assert "Estimated Budget Breakdown" in result
    assert "Flights" in result
    assert "Hotel/Stay" in result
    assert "Meals & Dining" in result
    assert "Budget Status" in result
