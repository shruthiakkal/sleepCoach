# sleepCoach

An LLM Engineering Learning Project (FastAPI + Groq + Prompt Design).

This repository is not a production sleep coaching system and not a medical application.

It is a hands-on learning project created to help me (a senior backend engineer) understand how modern LLM systems are built in practice - specifically:

- How to integrate LLM APIs into backend services
- How prompt structure affects output quality
- How context construction and feature summarization matter more than raw data
- How to iteratively evolve prompts and system design

## Version 1 - LLM API Fundamentals

Learn the mechanics of calling an LLM from a backend service.
At this stage, the LLM behaves like a text completion API - results are generic unless carefully guided.

How to Test
Once the server is running, you can test the endpoint using curl or FastAPI's built-in Swagger UI at http://127.0.0.1:8000/docs

Example Request:
POST /coach/analyze

{
"user_name": "Lisa",
"avg_hrv": 45,
"tags": ["late_workout", "stressful_day"]
}

## Version 2 - Context & Feature Engineering

Move beyond raw prompting and introduce structured context.

- Processes 7 days of sleep data instead of a single request
- Performs manual feature engineering

LLMs produce far better outputs when given pre-digested context, not unfiltered data.

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

## Version 3 - Data-Grounded & Prompt-Oriented Design

Experiment with data-grounded prompts and prompt modularity.

- Prompts are generated from a dataset
- Prompt logic is externalized into a dedicated generator
- Conditional instructions are embedded in the prompt itself

The dataset is used only to ground prompts, not to train or validate any model.
