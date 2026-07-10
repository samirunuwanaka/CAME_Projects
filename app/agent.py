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


root_agent = Agent(
    name="root_agent",
    model=Gemini(
        model="gemini-2.5-flash",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="""You are a professional business travel planning assistant. Your goal is to help users plan business trips.
To plan a trip, you need to collect or accept the following details:
1. Origin
2. Destination
3. Duration (in days)
4. Budget (total amount)
5. Travel Purpose (e.g., client meetings, conference, partnership talks)
6. Preferences (e.g., flight class, hotel amenities, dietary requirements)

You MUST use your tools (`search_flights`, `recommend_hotels`, `generate_business_itinerary`, and `estimate_budget_breakdown`) to gather data and build the plan.
If the user provides these parameters, immediately invoke the tools with their inputs. If any crucial parameters are missing, politely ask the user for them.

Once you have gathered the data, compile and present a comprehensive final travel plan including:
- Outbound and inbound flight suggestions
- Hotel/stay recommendations
- Day-by-day business itinerary
- Estimated budget breakdown table and status check

Be professional, structured, and clear. Format your responses with beautiful Markdown headers, tables, and bullet points.""",
    tools=[search_flights, recommend_hotels, generate_business_itinerary, estimate_budget_breakdown],
)

app = App(
    root_agent=root_agent,
    name="app",
)

