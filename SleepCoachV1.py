import os
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel 
from typing import List
from groq import Groq
from dotenv import load_dotenv

'''V1 code - getting familiar on how to use LLM services'''


# load env variables
load_dotenv()

# Groq setup
api_key = os.getenv("GROQ_API_KEY")
port = int(os.getenv("PORT", 8000))
if not api_key:
    print("Warning: GROQ_API_KEY is missing!")
client = Groq(api_key=api_key)
app = FastAPI()

class SleepData(BaseModel):
    user_name: str
    avg_hrv: int
    tags: List[str]

@app.post("/coach/analyze")
async def analyze_sleep(data: SleepData):
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="SleepCoach is currently taking a nap (Service Unavailable). Please check back later!"
        )
    # Context Logic
    context = "User had a late workout and caffeine." if "late_workout" in data.tags else ""
    
    # Prompt
    prompt = f"As a sleep coach, analyze this: {data.json()}. Context: {context}. Give 3 tips."

    # 3. Call te model - Llama 3.3 70B - sends prompt to this model
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return {"advice": completion.choices[0].message.content}


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)

