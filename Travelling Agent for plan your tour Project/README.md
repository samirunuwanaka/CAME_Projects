# ✈️ AeroTrip AI — Multi-Agent Travel Planner & Logistics Suite

!["agent structure"](agent%20structure.png)

A state-of-the-art AI application built with **Google Agent Development Kit (ADK 2.0)** featuring a multi-agent sub-agent architecture, automated travel guardrails, prerequisites verification, and a modern web dashboard.

---

## 🌟 Key Features & Sub-Agent Architecture

1. 🛫 **Flight Planner Sub-Agent (`flight_planner_agent`)**:
   - Searches flight routes, airline options, departure/arrival schedules, cabin class pricing, and flight amenities.
   - Evaluates flight-specific travel prerequisites (passport 6-month validity rule, eTA/eVisa requirements, TSA guidelines).

2. 📍 **Places Explorer Sub-Agent (`places_explorer_agent`)**:
   - Discovers top tourist attractions, cultural landmarks, executive leisure spots, and local dining hotspots.
   - Tailors recommendations based on traveler interests, trip duration, and dietary preferences.

3. 🛡️ **Travel Guardrails Engine**:
   - Enforces input validation (origin vs destination checks), trip duration boundaries (1–60 days), budget feasibility checks ($50/day min + flight baseline), and travel advisories.

4. 📋 **Prerequisites Verification System**:
   - Prompts travelers for mandatory prerequisites before departure: Passport expiration, Visa / entry clearance, Health/Vaccines, Travel Insurance, and Corporate payment cards.

5. 🎨 **Beautiful Glassmorphism Web Interface**:
   - Modern dark slate UI with vibrant gradients, sub-agent status mesh monitor, tabbed results view, timeline itinerary renderer, budget visualizer, and interactive AI assistant chat widget.

---

## 📂 Project Structure

```text
travel-planning-agent/
├── app/                      # Core agent & API implementation
│   ├── agent.py              # Sub-agents (flight_planner, places_explorer), root agent, guardrails, & tools
│   ├── fast_api_app.py       # FastAPI web app, sub-agent REST API endpoints, & static routes
│   ├── static/               # Beautiful Web Application Frontend (HTML, CSS, JS)
│   └── app_utils/            # Utilities for telemetry, A2A, and adapters
├── tests/                    # Unit and integration test suites
│   ├── unit/                 # Unit tests for tools, sub-agents, guardrails, and API endpoints
│   └── integration/          # E2E integration and stream tests
├── pyproject.toml            # Dependencies and project metadata
└── README.md                 # Project documentation
```

---

## 🛠️ Requirements & Setup

### 1. Configure Gemini API Key
Link the project to your Gemini API key:
1. Obtain an API key from [Google AI Studio](https://aistudio.google.com/).
2. Create or update `.env` in the root directory:
   ```env
   GOOGLE_GENAI_USE_VERTEXAI=false
   GEMINI_API_KEY=YOUR_FREE_API_KEY_HERE
   ```

### 2. Run the Web Dashboard & Sub-Agent API
To launch the FastAPI server with the Web Dashboard UI:
```bash
.\.venv\Scripts\python -m uvicorn app.fast_api_app:app --reload --port 8000
```
Open your browser and navigate to:
👉 **`http://localhost:8000/`** (or `http://localhost:8000/ui`)

---

## 🧪 Testing

To run the unit test suite:
```bash
.\.venv\Scripts\python -m pytest tests/unit
```

---

## 🌌 Built with Antigravity
> **Development Stamp:** `Antigravity Multi-Agent & UI Edition 🌌`

