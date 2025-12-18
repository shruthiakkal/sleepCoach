# sleepCoach

Sleep Coach AI (V3) - Occupational Health Edition

What's New in V3?

V3 introduces Contextual Grounding. Instead of the user providing their sleep data manually, the system fetches detailed profiles from a comprehensive sleep health dataset based on a user_id.

Key Enhancements:

  - Data Integration: Utilizes the Sleep Health and Lifestyle Dataset.

  - Role-Based Prompting: Assigns a specific persona to the LLM ("Expert Sleep Coach in Occupational Health").

  - Conditional Logic: The prompt generator now includes "If/Then" logic, guiding the LLM to focus on specific stressors (e.g., burnout for Doctors, sedentary issues for Software Engineers).



Sleep Coach AI (V2) - Weekly Insights

The V2 Sleep Coach upgrades from daily tips to long-term trend analysis. By aggregating a full week of sleep metrics and lifestyle habits, it identifies patterns that a single-day analysis might miss.

Key Upgrades in V2
- Processes a collection of OneDaySleep objects to understand user behavior over time.
- Instead of generic tips, the model now focuses on "One Big Change" based on a 7-day lookback.

API Endpoint: /coach/weekly/analysis

Sample Request Payload:
{
  "user_name": "Jordan",
  "last_7_days": [
    {"date": "2023-10-01", "hrv": 55, "score": 82, "tags": ["late_workout", "caffeine"]},
    {"date": "2023-10-02", "hrv": 48, "score": 70, "tags": ["stress"]},
    {"date": "2023-10-03", "hrv": 60, "score": 88, "tags": []},
    {"date": "2023-10-04", "hrv": 52, "score": 75, "tags": ["late_workout"]},
    {"date": "2023-10-05", "hrv": 58, "score": 80, "tags": []},
    {"date": "2023-10-06", "hrv": 45, "score": 65, "tags": ["alcohol"]},
    {"date": "2023-10-07", "hrv": 62, "score": 90, "tags": ["meditation"]}
  ]
}


Sleep Coach AI (V1)

A simple FastAPI service that acts as a personalized sleep coach. This project demonstrates how to integrate the Groq SDK with Llama 3.3 70B to provide health insights based on user data.

Overview

This application takes user sleep metrics (HRV and lifestyle tags) and generates three actionable coaching tips using an LLM. It serves as a foundational example of:
- Building RESTful APIs with FastAPI.
- Data validation using Pydantic.
- Prompt engineering with contextual logic
- Interacting with high-performance LLMs via Groq.

How to Test

Once the server is running, you can test the endpoint using curl or FastAPI's built-in Swagger UI at http://127.0.0.1:8000/docs

Example Request:
POST /coach/analyze

{
  "user_name": "Lisa",
  "avg_hrv": 45,
  "tags": ["late_workout", "stressful_day"]
}
