import os
from fastapi import FastAPI,HTTPException
from groq import Groq
from dotenv import load_dotenv

from SleepCoachForProfessionalsPrompts import generate_coach_prompt

# load env variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

app = FastAPI()

@app.post("/coach/suggestions")
async def analyse_user_lifestyle_affecting_sleep(user_id):
    # user specific prompts based on profession
    prompt = generate_coach_prompt(int(user_id))

    if prompt is None:
        raise HTTPException(
            status_code=404, 
            detail=f"User ID {user_id} not found"
        )



    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return {"sleep_coaching": completion.choices[0].message.content}


if __name__== "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



    


