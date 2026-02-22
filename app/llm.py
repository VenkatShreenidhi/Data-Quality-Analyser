import os 
from dotenv import load_dotenv
import requests

def analyse_incident(prompt:str)->str:
    """
    sends the prompt to openAI and returns the LLM's response 
    as a string
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]
