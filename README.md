# 🌍 Agentic AI Travel Planner

## 1. Overview

This project is an end-to-end **agentic travel planning** application that generates complete, structured travel itineraries with **real-time data**. It combines a FastAPI backend with a Streamlit front-end and orchestrates multi-step reasoning (planning, budgeting, and live information lookup) using **LangGraph** + **LangChain tools**. The system fetches live signals such as **weather** using open APIs and produces a detailed travel plan with itinerary, costs, and recommendations.

The application is fully containerised with separate Docker images for the **back-end** and **front-end**, orchestrated via `docker-compose`.

---

## Live Interface

<p align="center">
  <!-- Replace with your screenshot URL -->
  <img width="1600" alt="trip-planner-ui" src="https://github.com/user-attachments/assets/REPLACE_WITH_YOUR_IMAGE" />
</p>

> **Figure 1.** Streamlit front-end showcasing chat-based travel planning and structured plan output.

---

## 2. Motivation

Planning travel typically means bouncing between multiple sites—weather, maps, attractions, budget calculators, and transport details. Static itineraries don’t adapt to user preferences or real-time conditions.

This project aims to provide an **AI travel assistant** that can:

- understand trip intent (days, budget, style, location);
- fetch relevant live context (e.g., weather);
- generate actionable itineraries with clear structure; and
- estimate costs and per-day budgets programmatically.

---

## 3. Goals & Objectives

1. **Agentic planning.** Use a LangGraph state machine to break planning into steps (intent → tools → plan).
2. **Real-time signals.** Pull live data (weather) via open APIs (OpenWeatherMap).
3. **Accurate budgeting.** Provide a detailed cost breakdown using calculator tools (hotel, daily budget, total expense).
4. **Seamless deployment.** One-command `docker-compose` to spin up both backend and UI locally.

---

## 4. Solution Approach

### 4.1 Agentic Planning Pipeline


<p align="center">
  <!-- Replace with your architecture diagram if you have one -->
  <img width="520" alt="architecture" src="https://github.com/user-attachments/assets/REPLACE_WITH_YOUR_DIAGRAM" />
</p>

**Key components**
1. **Intent parsing:** Extract destination, duration, and constraints from user prompt.
2. **Tool execution:** Fetch live weather + compute expenses through tools.
3. **Plan generation:** Generate a clean markdown plan including itinerary + costs + recommendations.
4. **Response formatting:** Streamlit renders the plan with headings, bullet points, and sections.

---

### 4.2 Front-end

The Streamlit UI mimics a chat interface and calls the backend REST endpoint. Output is formatted in Markdown and includes generated timestamp, cost summary, and plan sections.

---

## 5. Tech Stack

| Layer | Technology | Purpose |
|------|------------|---------|
| LLM / Reasoning | OpenAI / Groq | Travel plan generation |
| Orchestration | LangChain + LangGraph | Tool binding & agentic state graph |
| Live Data | OpenWeatherMap API | Weather + forecast |
| Back-end | FastAPI + Uvicorn (via uv) | REST API |
| Front-end | Streamlit | Chat UI |
| Infra | Docker + docker-compose | Containerized deployment |
| Config | python-dotenv | Environment variables |

---

## 6. Repository Layout


---

## 7. Getting Started

### 7.1 Local Development (Python ≥ 3.11)

```bash
# Clone & enter
git clone https://github.com/harshali1226/Trip_Planner.git
cd Trip_Planner

# Install uv and sync deps
pip install uv
uv sync

# Environment
cp .env.example .env  # add API keys

# Backend
uv run uvicorn main:app --host 0.0.0.0 --port 8000

# Frontend
uv run streamlit run app.py
```

### 7.2 Containerised Deployment

#### 1. Build images (optional – Compose will build if missing):
```bash
docker build -f Dockerfile.backend -t trip-planner-backend:latest .
docker build -f Dockerfile.frontend -t trip-planner-frontend:latest .
```

#### 2. Start the stack:
```bash
docker compose up --build
```

#### 3. Shut down:
```bash
docker compose down
```

### 7.3 Environment Variables

Minimum keys required in .env:

```env
OPENAI_API_KEY=...
GROQ_API_KEY=...
GOOGLE_API_KEY=...
GPLACES_API_KEY=...
FOURSQUARE_API_KEY=...
TAVILAY_API_KEY=...
OPENWEATHERMAP_API_KEY=...
EXCHANGE_RATE_API_KEY=...
```


### 8. Usage

Open the Streamlit UI and enter a prompt like:

- “Plan a trip to Dubai for 2 days with budget breakdown”
- “Create an off-beat 5-day itinerary for Himachal Pradesh”
- “Plan a weekend trip to NYC with daily expense estimate”

The app returns:
- Day-by-day itinerary
- Hotel recommendations with approximate costs
- Attractions, activities, and restaurant suggestions
- Transportation options
- Live weather summary (when available)
- Detailed cost breakdown with per-day budget estimate

---

### 9. Roadmap

- 🏨 Add real hotel and restaurant pricing integrations  
- 🗺️ Maps and geocoding support for precise locations  
- 🧠 Preference memory (budget, travel style, pace, food preferences)  
- 📊 Cost comparison across multiple itinerary options  
- ☁️ Deploy to Hugging Face / Render / AWS  

---

### 10. License

This project is released under the **MIT License**.
