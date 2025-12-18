import pandas as pd

# Load dataset
# https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset?resource=download
try:
    df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
except FileNotFoundError:
    print("Ensure that the CSV file is in the folder")


def generate_coach_prompt(user_id):
    '''Prompt engineering'''
    # fetch a specific user from data
    user_rows = df[df['Person ID'] == user_id]

    if user_rows.empty:
        return None
    
    user = user_rows.iloc[0]

    # logics to help LLM
    job = user['Occupation']
    duration = user['Sleep Duration']
    quality = user['Quality of Sleep']
    steps = user['Daily Steps']
    disorder = user['Sleep Disorder']

    # Custom prompt engineering based on the dataset columns
    prompt = f"""
    ROLE: You are an expert Sleep Coach specializing in occupational health.    
    USER DATA:
    - Occupation: {job}
    - Sleep: {duration} hours (Quality: {quality}/10)
    - Activity: {steps} steps per day
    - Health Note: {disorder if disorder != 'None' else 'No diagnosed disorders'}

    COACHING TASK:
    
    If the sleep quality is below 6, analyze why a {job} might be struggling with a sleep quality of {quality}/10. 
    If they have low steps, mention physical movement. 
    If they are a 'Software Engineer' or 'Doctor', mention mental burnout.
    If the score is 8 or above provide how actionable tips to get a perfect 10 score.
    If the score is less than 8 provide 1 actionable tip each based on their occupation, health and stress maintenance.
    """
    return prompt

