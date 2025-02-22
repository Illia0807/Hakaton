from dotenv import load_dotenv
import requests
import json
import os
load_dotenv()
token_ai = os.getenv('TOKEN_AI')
API_URL = "https://api-inference.huggingface.co/models/google/gemma-2-2b-it"
HEADERS = {"Authorization": token_ai}

def generate_bedtime_story(name: str, role: str, location: str) -> str:
    
    prompt = f"Write a short bedtime story about a {role} named {name} who is in {location}. Make the story fun and surprising."

    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    
    if response.status_code == 200:
        response_json = response.json()
        
        return response_json[0]['generated_text']
    else:
        
        return f"Ошибка API: {response.status_code}, {response.text}"


