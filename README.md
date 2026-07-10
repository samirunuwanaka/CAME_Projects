# ✈️ Travel Planning Agent

A professional AI agent designed using the Google Agent Development Kit (ADK) to help users plan business trips. 

This agent accepts trip parameters (origin, destination, duration, budget, travel purpose, and preferences) and orchestrates a set of tools to generate:
- 🛫 **Flight suggestions** (outbound/inbound schedules, airlines, and price classes)
- 🏨 **Hotel/stay recommendations** (business-friendly hotel choices with rates and amenities)
- 📅 **Day-by-day business itineraries** (tailored to the trip's purpose and preferences)
- 📊 **Estimated budget breakdowns** (detailed cost breakdown compared against the target budget)

---

## 🚀 Built with Antigravity
> [!NOTE]
> This project was developed with the assistance of **Antigravity**, an agentic AI coding assistant from Google DeepMind. It was scaffolded, designed, and implemented with agentic AI aid to ensure high quality and adhere to ADK best practices.
>
> **Development Stamp:** `Antigravity Agent Assisted 🌌`

---

## 📂 Project Structure

```text
travel-planning-agent/
├── app/                      # Core agent implementation
│   ├── agent.py              # Agent definition, system instructions, and planning tools
│   ├── fast_api_app.py       # FastAPI application and route endpoints
│   └── app_utils/            # Utilities for telemetry, A2A, and adapters
├── tests/                    # Unit and integration test suites
│   ├── unit/                 # Unit tests for tools and logic
│   └── integration/          # E2E integration and stream tests
├── pyproject.toml            # Dependencies and project metadata
└── README.md                 # Project documentation
```

## 🛠️ Requirements & Setup

Before you begin, ensure you have:
- **pipenv**: For virtual environment and dependency management.
- **Python**: Version 3.11+.
- **google-agents-cli**: Installed within your environment.

### 1. Configure the Gemini API Key (Free Tier)
To resolve the `default Credental error` (which occurs when Vertex AI is enabled without active GCP credentials), you can link the project to the free Gemini API key from Google AI Studio:
1. Go to [Google AI Studio](https://aistudio.google.com/) and create a free API key.
2. Open the `.env` file in the root of the project.
3. Verify that `GOOGLE_GENAI_USE_VERTEXAI` is set to `false`:
   ```env
   GOOGLE_GENAI_USE_VERTEXAI=false
   ```
4. Paste your API key into the `GEMINI_API_KEY` field:
   ```env
   GEMINI_API_KEY=YOUR_FREE_API_KEY_HERE
   ```

### 2. Initialize Virtual Environment
Set up your virtualenv with pipenv:
```bash
# Force virtualenv to be created inside the project directory
$env:PIPENV_VENV_IN_PROJECT="1"
$env:PIPENV_VIEW_IN_PROJECT="1"

# Install all project dependencies
pipenv install
```

### 3. Run the Agent Playground
Start the local agent playground for testing:
```bash
pipenv run agents-cli playground
```
This launches a web interface where you can chat with the travel planning agent and inspect its tool calls.

---

## ⚙️ Core Tools

The agent leverages specialized python functions registered as tools:
1. `search_flights`: Generates simulated flight options based on origin, destination, and dates.
2. `recommend_hotels`: Finds lodging fitting the target budget.
3. `generate_business_itinerary`: Builds a structured, purpose-driven schedule for the stay.
4. `estimate_budget_breakdown`: Compares costs (flights, hotels, meals, transit, buffer) against the budget.

---

## 🧪 Testing

To run the integration and unit tests:
```bash
pipenv run pytest tests/unit tests/integration
```

---

## 🌌 Future Development using Antigravity

This project is pre-integrated with **Antigravity**, Google's agentic AI coding assistant. You can use the Antigravity CLI (`agy`) directly in the project directory to develop new features, debug errors, or add tests.

### How to use Antigravity for development:
1. Open a terminal in the project directory:
   ```bash
   cd travel-planning-agent
   ```
2. Launch the Antigravity interactive prompt session:
   ```bash
   agy
   ```
3. Prompt Antigravity to perform tasks. For example:
   - **Adding Features**: `"Add a new tool in agent.py to fetch live weather details for the destination city, and include it in the itinerary summary."`
   - **Running/Fixing Tests**: `"Run pytest to check if all tests pass, and fix any import errors."`
   - **Adding Database Persistence**: `"Link the agent to a database to save the generated itineraries for later retrieval."`
   - **Refactoring**: `"Refactor the hotel recommendation tool to prioritize hotels that have a gym."`

Antigravity will automatically analyze the codebase context via `GEMINI.md`, modify code files, run terminal commands, and verify changes.

---
*Developed with 💙 and the aid of Antigravity AI.*
