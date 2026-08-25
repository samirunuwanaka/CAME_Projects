import datetime
from zoneinfo import ZoneInfo

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types

load_dotenv()



def search_flights(origin: str, destination: str, duration_days: int) -> str:
    """Search for available business-friendly flights between origin and destination.

    Args:
        origin: The starting airport code or city name (e.g., "SFO" or "San Francisco").
        destination: The destination airport code or city name (e.g., "NYC" or "New York").
        duration_days: The length of the trip in days to determine return flight dates.

    Returns:
        A formatted markdown string listing flight suggestions (outbound and inbound)
        with airline details, departure/arrival times, class of travel, and prices.
    """
    h = sum(ord(c) for c in origin + destination)
    
    today = datetime.date.today()
    departure_date = today + datetime.timedelta(days=14)
    return_date = departure_date + datetime.timedelta(days=duration_days)
    
    price_economy = 250.0 + (h % 300)
    price_business = price_economy * 2.5
    
    airline1 = "Delta Air Lines" if h % 2 == 0 else "United Airlines"
    airline2 = "American Airlines" if h % 3 == 0 else "JetBlue"
    
    return f"""### Flight Suggestions: {origin} to {destination}
**Outbound Flight: {departure_date.strftime('%B %d, %Y')}**
1. **{airline1} FL1024**
   - Departure: 08:30 AM | Arrival: 11:45 AM
   - Duration: Direct
   - Price: Economy: ${price_economy:.2f} | Business: ${price_business:.2f}
   - Amenities: Wi-Fi, power outlets, business-class priority boarding.
2. **{airline2} FL4092**
   - Departure: 02:15 PM | Arrival: 05:30 PM
   - Duration: Direct
   - Price: Economy: ${(price_economy - 30):.2f} | Business: ${(price_business - 50):.2f}
   - Amenities: Wi-Fi, free drinks.

**Inbound Flight: {return_date.strftime('%B %d, %Y')}**
1. **{airline1} FL2048**
   - Departure: 05:00 PM | Arrival: 08:15 PM
   - Duration: Direct
   - Price: Included in roundtrip (Economy: ${price_economy:.2f} | Business: ${price_business:.2f} total)
2. **{airline2} FL5084**
   - Departure: 08:00 AM | Arrival: 11:15 AM
   - Duration: Direct
   - Price: Included in roundtrip (Economy: ${(price_economy - 20):.2f} | Business: ${(price_business - 40):.2f} total)
"""


def recommend_hotels(destination: str, budget: float, duration_days: int, preferences: str = "") -> str:
    """Recommend business-friendly hotels or stays in the destination city.

    Args:
        destination: The destination city name (e.g., "New York", "Chicago").
        budget: The total budget allocated for the trip.
        duration_days: The number of nights to stay.
        preferences: Optional traveler preferences (e.g., "near convention center", "quiet room", "gym", "free breakfast").

    Returns:
        A selection of hotel options with nightly rates, total rates, key amenities, and location highlights.
    """
    h = sum(ord(c) for c in destination)
    
    # Establish nightly rates based on budget and duration
    avg_nightly_budget = budget / (duration_days if duration_days > 0 else 1)
    target_rate = max(100.0, avg_nightly_budget * 0.45)
    
    hotel1_rate = target_rate * 0.95
    hotel2_rate = target_rate * 1.2
    
    hotel1_total = hotel1_rate * duration_days
    hotel2_total = hotel2_rate * duration_days
    
    hotel1_name = "The Executive Inn & Suites" if h % 2 == 0 else "Apex Business Hotel"
    hotel2_name = "Grand Plaza Hotel" if h % 2 == 0 else "Summit Heights Hotel"
    
    pref_match = f"- Matches preferences: {preferences}" if preferences else "- Tailored for business travelers."
    
    return f"""### Hotel/Stay Recommendations in {destination}
1. **{hotel1_name}** ⭐⭐⭐⭐
   - **Nightly Rate**: ${hotel1_rate:.2f} | **Total for {duration_days} nights**: ${hotel1_total:.2f}
   - **Key Amenities**: Free high-speed Wi-Fi, 24/7 business center, executive desk in room, gym, hot breakfast included.
   - **Location**: 5 minutes walk from city center/financial district.
   - {pref_match}

2. **{hotel2_name} (Premium Option)** ⭐⭐⭐⭐⭐
   - **Nightly Rate**: ${hotel2_rate:.2f} | **Total for {duration_days} nights**: ${hotel2_total:.2f}
   - **Key Amenities**: Ultra-fast fiber Wi-Fi, soundproof rooms, in-room conferencing facilities, premium fitness center, concierge service.
   - **Location**: Adjacent to major transit hub and business square.
   - {pref_match}
"""


def generate_business_itinerary(destination: str, duration_days: int, travel_purpose: str, preferences: str = "") -> str:
    """Generate a structured day-by-day business itinerary.

    Args:
        destination: The destination city name.
        duration_days: The number of days for the trip.
        travel_purpose: The main goal of the trip (e.g., "client meetings", "conference", "partnership talks").
        preferences: Optional traveler preferences (e.g., "prefer morning meetings", "vegetarian meals", "sightseeing").

    Returns:
        A detailed day-by-day itinerary detailing professional meetings, travel, networking, meals, and rest time.
    """
    days = max(1, duration_days)
    itinerary = [f"### Day-by-Day Business Itinerary: {destination} (Purpose: {travel_purpose})"]
    
    for i in range(1, days + 1):
        if i == 1:
            day_schedule = f"""#### Day {i}: Arrival & Prep
- **08:30 AM**: Flight departure and transit.
- **12:00 PM**: Hotel check-in and settling in.
- **01:30 PM**: Working lunch near the hotel.
- **03:00 PM - 05:00 PM**: Preparation and prep-work for "{travel_purpose}" in the hotel's business center.
- **07:00 PM**: Welcome dinner (Preferences: {preferences or 'Standard business casual dining'})."""
        elif i == days:
            day_schedule = f"""#### Day {i}: Wrap-up & Departure
- **08:30 AM - 10:00 AM**: Final wrap-up meetings or email check-in.
- **11:00 AM**: Check-out of the hotel.
- **12:00 PM**: Working lunch at the airport.
- **02:00 PM**: Flight departure back home.
- **06:00 PM**: Arrival and completion of trip."""
        else:
            day_schedule = f"""#### Day {i}: Core Meetings & Networking
- **08:00 AM**: Breakfast at the hotel.
- **09:30 AM - 12:00 PM**: High-priority sessions/meetings for {travel_purpose}.
- **12:30 PM - 02:00 PM**: Networking lunch with partners or local team.
- **02:30 PM - 05:00 PM**: Follow-up sessions, presentations, or site visits.
- **06:30 PM**: Team or client dinner (Preferences: {preferences or 'Standard business casual dining'}).
- **08:30 PM**: Evening wrap-up or leisure time."""
        itinerary.append(day_schedule)
        
    return "\n\n".join(itinerary)


def estimate_budget_breakdown(origin: str, destination: str, duration_days: int, total_budget: float) -> str:
    """Calculate and estimate the detailed budget breakdown for the business trip.

    Args:
        origin: The origin city.
        destination: The destination city.
        duration_days: The number of days of the trip.
        total_budget: The total budget allocated by the user.

    Returns:
        A detailed cost breakdown (flights, hotels, meals, local transport, buffer) and comparison with the total budget.
    """
    h = sum(ord(c) for c in origin + destination)
    
    flight_est = 250.0 + (h % 300)
    hotel_est_nightly = 150.0 + (h % 100)
    hotel_est_total = hotel_est_nightly * max(1, duration_days - 1)
    
    meals_est = 75.0 * duration_days
    transport_est = 50.0 * duration_days
    buffer_est = (flight_est + hotel_est_total + meals_est + transport_est) * 0.15
    
    total_est = flight_est + hotel_est_total + meals_est + transport_est + buffer_est
    difference = total_budget - total_est
    
    status = ""
    if difference >= 0:
        status = f"✅ **Within Budget**: Your total estimated cost (${total_est:.2f}) fits within your budget (${total_budget:.2f}) with a surplus of **${difference:.2f}**."
    else:
        status = f"⚠️ **Budget Exceeded**: The estimated cost (${total_est:.2f}) exceeds your budget (${total_budget:.2f}) by **${abs(difference):.2f}**. Consider opting for economy flights or a budget-friendly hotel option."
        
    return f"""### Estimated Budget Breakdown (Total Budget: ${total_budget:.2f})

| Expense Category | Daily Estimate | Total Estimated Cost | Percentage |
| :--- | :--- | :--- | :--- |
| **Flights (Roundtrip)** | - | ${flight_est:.2f} | {(flight_est/total_est*100):.1f}% |
| **Hotel/Stay ({max(1, duration_days - 1)} nights)** | ${hotel_est_nightly:.2f} | ${hotel_est_total:.2f} | {(hotel_est_total/total_est*100):.1f}% |
| **Meals & Dining ({duration_days} days)** | $75.00 | ${meals_est:.2f} | {(meals_est/total_est*100):.1f}% |
| **Local Transport (Cabs, Transit)** | $50.00 | ${transport_est:.2f} | {(transport_est/total_est*100):.1f}% |
| **Emergency Buffer (15%)** | - | ${buffer_est:.2f} | {(buffer_est/total_est*100):.1f}% |
| **Total Estimated** | - | **${total_est:.2f}** | **100%** |

**Budget Status:**
{status}
"""


def check_flight_prerequisites(origin: str, destination: str, passport_valid_months: int = 6, visa_status: str = "Required") -> str:
    """Check travel prerequisites for flights including passport validity, visa, and transit requirements.

    Args:
        origin: The origin airport or city code.
        destination: The destination airport or city code.
        passport_valid_months: Number of months remaining on passport before expiration.
        visa_status: Traveler's visa status or requirement state.

    Returns:
        A markdown report of flight & international travel prerequisites and required documentation.
    """
    valid = passport_valid_months >= 6
    status_icon = "✅" if valid else "⚠️"
    
    return f"""### 🛂 Flight & Travel Prerequisites Check ({origin} ✈️ {destination})
{status_icon} **Passport Validity**: {passport_valid_months} months remaining (Minimum requirement: 6 months from travel date).
📋 **Visa Status**: {visa_status} - Ensure electronic travel authorization (eTA/eVisa) or tourist/business visa is granted prior to departure.
🏥 **Health & Security Requirements**: Standard TSA/Airport screening guidelines apply. Carry digital copy of travel insurance & proof of accommodation.
💡 **Pre-departure Checklist**:
- Verify passport expiration date is past 6 months.
- Print/save flight booking confirmation and hotel voucher.
- Confirm business invitation letter if traveling for corporate meetings.
"""


def search_places_to_visit(destination: str, travel_purpose: str = "general", interests: str = "sightseeing, dining", duration_days: int = 3) -> str:
    """Discover top places to visit, attractions, cultural landmarks, and local highlights in the destination city.

    Args:
        destination: The destination city name (e.g. "Paris", "Tokyo", "New York").
        travel_purpose: The purpose of travel (e.g. "business", "leisure", "conference").
        interests: Key interests (e.g. "museums", "architecture", "food", "parks").
        duration_days: Trip duration in days.

    Returns:
        A curated list of top places to visit categorized by attraction type with estimated durations and highlights.
    """
    h = sum(ord(c) for c in destination)
    
    attractions = [
        ("Downtown Cultural & Arts District", "Explore iconic landmarks, historic architecture, and world-class museum exhibitions.", "2-3 hours"),
        ("Skyline Observation Deck & Financial Hub", "Breathtaking panoramic views of the city skyline, perfect for evening unwinding or casual business catch-ups.", "1.5 hours"),
        ("Riverside Promenade & Botanical Gardens", "Scenic waterfront walkways with lush gardens and open-air cafes.", "2 hours"),
        ("Historic Market Square & Artisan Quarter", "Bustling local market filled with local crafts, specialty coffees, and authentic street dining.", "2 hours")
    ]
    
    selected_attractions = attractions[:min(len(attractions), max(2, duration_days))]
    
    items_md = ""
    for idx, (name, desc, est_time) in enumerate(selected_attractions, 1):
        items_md += f"""{idx}. **{name}** 🌟
   - **Highlights**: {desc}
   - **Recommended Time**: {est_time}
   - **Best Visit Time**: Morning or Late Afternoon\n"""
        
    return f"""### 📍 Places to Visit in {destination} (Curated by Places Explorer Sub-Agent)
*Interests: {interests} | Trip Duration: {duration_days} Days*

{items_md}
💡 **Local Tip**: Combine sightseeing during late afternoon slots after business meetings to make the most of your stay!
"""


def recommend_local_dining(destination: str, dietary_pref: str = "general") -> str:
    """Recommend top local dining, executive restaurants, and culinary hotspots in the destination city.

    Args:
        destination: The target city.
        dietary_pref: Optional dietary preference (e.g. "vegetarian", "vegan", "gluten-free", "seafood", "fine dining").

    Returns:
        A formatted list of top dining spots with cuisine details and atmosphere.
    """
    h = sum(ord(c) for c in destination)
    r1_name = "The Capital Grille & Bistro" if h % 2 == 0 else "Bistro de Paris Executive Dining"
    r2_name = "Zen Garden & Farm-to-Table" if h % 2 == 0 else "Skyline Terrace Dining"
    
    return f"""### 🍽️ Local Dining & Culinary Spots in {destination}
1. **{r1_name}** (Fine Business Dining) ⭐⭐⭐⭐⭐
   - **Cuisine**: Contemporary Continental & Prime Steaks
   - **Atmosphere**: Quiet, elegant indoor seating ideal for client dinners and networking.
   - **Dietary Accommodations**: {dietary_pref or 'Options available for all diets'}.

2. **{r2_name}** (Casual & Authentic Local) ⭐⭐⭐⭐
   - **Cuisine**: Seasonal Organic & Fusion Specialties
   - **Atmosphere**: Relaxed garden ambiance with swift service for quick lunches.
   - **Dietary Accommodations**: Extensive vegetarian & vegan options.
"""


def validate_travel_guardrails(origin: str, destination: str, total_budget: float, duration_days: int) -> str:
    """Validate travel parameters against strict safety, budget, input integrity, and duration guardrails.

    Args:
        origin: Origin city/airport.
        destination: Destination city/airport.
        total_budget: Total budget set for the trip.
        duration_days: Trip duration in days.

    Returns:
        Guardrails status evaluation report (Passed, Warnings, or Blocked).
    """
    issues = []
    warnings = []
    
    # Input Guardrail
    if not origin or not destination:
        issues.append("Origin and Destination cannot be empty.")
    elif origin.strip().lower() == destination.strip().lower():
        issues.append("Origin and Destination cannot be the exact same location.")
        
    # Duration Guardrail
    if duration_days < 1:
        issues.append("Trip duration must be at least 1 day.")
    elif duration_days > 60:
        warnings.append("Trip duration exceeds 60 days. Extended stay policy approval may be required.")
        
    # Budget Guardrail
    min_flight_baseline = 200.0
    min_daily_cost = 50.0
    recommended_min_budget = min_flight_baseline + (min_daily_cost * max(1, duration_days))
    
    if total_budget < recommended_min_budget:
        warnings.append(f"Budget (${total_budget:.2f}) is lower than the recommended minimum (${recommended_min_budget:.2f}) for a {duration_days}-day trip.")
        
    status = "PASSED" if not issues else "BLOCKED"
    status_symbol = "🛡️✅" if status == "PASSED" else "🛡️🛑"
    
    result = f"""### {status_symbol} Travel Guardrails Evaluation Report
- **Overall Guardrail Status**: **{status}**
- **Origin / Destination Check**: {'Valid' if origin.lower() != destination.lower() else 'Error: Same origin and destination'}
- **Duration Check**: {duration_days} day(s) (Within allowed range)
- **Budget Integrity Check**: ${total_budget:.2f} (Minimum threshold: ${recommended_min_budget:.2f})
"""
    if issues:
        result += "\n🛑 **Blocking Issues Detected**:\n" + "\n".join(f"- {iss}" for iss in issues)
    if warnings:
        result += "\n⚠️ **Guardrail Warnings**:\n" + "\n".join(f"- {warn}" for warn in warnings)
        
    return result


def ask_prerequisites_checklist(destination: str, is_international: bool = True) -> str:
    """Generate a prerequisite checklist and ask for missing required inputs from the user before finalizing travel.

    Args:
        destination: Destination city/country.
        is_international: Whether the trip involves international border crossing.

    Returns:
        A list of required prerequisites and questions for missing travel information.
    """
    return f"""### 📋 Required Travel Prerequisites Checklist for {destination}

Before finalizing your travel plan, please ensure all required prerequisites are confirmed:

1. 🛂 **Passport Expiry Date**: Is your passport valid for at least 6 months past your travel dates?
2. 📄 **Visa / Entry Approval**: Do you have a valid Visa, eVisa, or ESTA clearance for {destination}?
3. 💉 **Health / Vaccine Records**: Have you checked health & entry regulations for {destination}?
4. 💳 **Corporate / Personal Payment Card**: Is your card notified for international/out-of-state transactions?
5. 🛡️ **Travel Insurance**: Is comprehensive medical and trip cancellation insurance active?

*If any prerequisite is missing, please inform your assistant so we can adjust flight bookings, buffer times, or documentation guidance accordingly.*
"""


# ---------------------------------------------------------------------------
# Define Specialized Sub-Agents
# ---------------------------------------------------------------------------

flight_planner_agent = Agent(
    name="flight_planner_agent",
    description="Sub-agent specializing in searching flights, analyzing airline schedules, ticket classes, and verifying flight prerequisites.",
    instruction="""You are an expert flight planning sub-agent.
Your goal is to handle all flight search logistics and verify flight travel prerequisites (passport 6-month validity, visa status).
Always provide detailed outbound/inbound flight recommendations with airlines, prices, times, and prerequisite checks.""",
    tools=[search_flights, check_flight_prerequisites],
)

places_explorer_agent = Agent(
    name="places_explorer_agent",
    description="Sub-agent specializing in discovering top places to visit, tourist attractions, cultural landmarks, and local dining experiences.",
    instruction="""You are a local places and tourism explorer sub-agent.
Your goal is to discover the best places to visit, iconic landmarks, outdoor spots, and top dining recommendations in the destination city.
Provide curated attraction recommendations with estimated visit times, highlights, and dining recommendations.""",
    tools=[search_places_to_visit, recommend_local_dining],
)


# ---------------------------------------------------------------------------
# Master Orchestrator Agent
# ---------------------------------------------------------------------------

root_agent = Agent(
    name="root_agent",
    model=Gemini(
        model="gemini-2.5-flash",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    description="Master travel orchestrator coordinating flight logistics, places to visit, guardrails, and prerequisites.",
    instruction="""You are a master business and travel planning assistant. Your goal is to help users plan trips by orchestrating specialized sub-agents and tools.

To plan a complete trip, gather or verify:
1. Origin & Destination
2. Duration (in days)
3. Budget (total amount)
4. Travel Purpose & Preferences
5. Travel Prerequisites (Passport validity, Visa status, Health guidelines)

Workflow & Requirements:
1. First, invoke `validate_travel_guardrails` to evaluate safety, budget feasibility, and input validity.
2. Delegate to or execute `flight_planner_agent` tools (`search_flights`, `check_flight_prerequisites`) to plan flight logistics and verify prerequisites.
3. Delegate to or execute `places_explorer_agent` tools (`search_places_to_visit`, `recommend_local_dining`) to find attractions and dining spots.
4. Execute `recommend_hotels` and `estimate_budget_breakdown` for stay and budget management.
5. Execute `generate_business_itinerary` and combine the business schedule, flight times, AND places to visit into a seamless day-by-day master plan.
6. Present the prerequisite checklist using `ask_prerequisites_checklist` if any travel details need confirmation.

Structure your final response with beautiful markdown headers, flight cards, places to visit lists, day-by-day combined itinerary, budget breakdown table, and guardrail reports.""",
    sub_agents=[flight_planner_agent, places_explorer_agent],
    tools=[
        search_flights,
        check_flight_prerequisites,
        search_places_to_visit,
        recommend_local_dining,
        recommend_hotels,
        generate_business_itinerary,
        estimate_budget_breakdown,
        validate_travel_guardrails,
        ask_prerequisites_checklist,
    ],
)

app = App(
    root_agent=root_agent,
    name="app",
)


