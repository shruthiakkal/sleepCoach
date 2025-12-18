import os
from fastapi import FastAPI
from pydantic import BaseModel 
from typing import List
from groq import Groq
from dotenv import load_dotenv


'''V2 code - we have 7 days of user data here for the sleep coach to come up with a tip to improve sleep'''

# load env variables
load_dotenv()

# Groq setup
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)
app = FastAPI()

class OneDaySleep(BaseModel):
    date: str
    hrv: int
    score: int
    tags: List[str]

class WeeklyReport(BaseModel):
    user_name:str
    last_7_days: List[OneDaySleep]


@app.post("/coach/weekly/analysis")
async def analyze_weekly_sleep(data: WeeklyReport):
    # Summarize the 7 days data - Pre -process
    # Imagine our sleep coach is based on tags like late workouts, hrv and avg sleep score

    days_count = len(data.last_7_days)
    
    if days_count == 0:
        return {"error": "Sleep coach does not have sleep data for analysis."}


    # This is called Feature Engineering, and it's how you build "Context-Aware" AI.
    late_workouts = sum(1 for day in data.last_7_days if "late_workout" in day.tags)
    avg_score = sum(day.score for day in data.last_7_days)/days_count

    # Manual Feature Engineering
    status = "Optimal" if avg_score > 80 else "Needs Improvement"

    # Context - this is need for AI
    context = f"""
    Over the last 7 days, the user had {late_workouts} late workouts.
    Their average sleep score is {avg_score:.1f}.
    """

    prompt = f"{context}\nDetailed Data: {data.json()}\nProvide a weekly summary and 1 big change for next week."

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return {"weekly_coaching": completion.choices[0].message.content}

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



'''
You can use the below request body

{
  "user_name": "user1",
  "last_7_days": [
    {
      "date": "2025-12-11T22:45:00+05:30",
      "hrv": 68,
      "score": 82,
      "tags": []
    },
    {
      "date": "2025-12-12T23:10:00+05:30",
      "hrv": 44,
      "score": 56,
      "tags": ["late_workout"]
    },
    {
      "date": "2025-12-13T23:20:00+05:30",
      "hrv": 41,
      "score": 54,
      "tags": ["late_workout"]
    },
    {
      "date": "2025-12-14T22:40:00+05:30",
      "hrv": 70,
      "score": 85,
      "tags": []
    },
    {
      "date": "2025-12-15T23:05:00+05:30",
      "hrv": 43,
      "score": 55,
      "tags": ["late_workout"]
    },
    {
      "date": "2025-12-16T23:15:00+05:30",
      "hrv": 42,
      "score": 53,
      "tags": ["late_workout"]
    },
    {
      "date": "2025-12-17T22:30:00+05:30",
      "hrv": 72,
      "score": 88,
      "tags": []
    }
  ]
}

	
Response body

{
  "weekly_coaching": "**Weekly Summary:**\nThe user, user1, had a mixed week in terms of sleep quality. Their average sleep score over the last 7 days was 67.6, which is slightly below the average. However, they had some good nights, with scores as high as 88. Unfortunately, they also had 4 late workouts, which seemed to negatively impact their sleep quality on those nights, with scores as low as 53.\n\n**Big Change for Next Week:**\nTo improve their sleep quality, I would recommend **avoiding late workouts**. On the days when they had late workouts, their sleep scores were significantly lower than on the days when they didn't. By adjusting their workout schedule to earlier in the day, they may be able to improve the quality of their sleep and increase their overall average sleep score. This change could have a significant impact on their overall well-being and energy levels."
}'''