# sleepCoach

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
