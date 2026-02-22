import json 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.prompt import build_prompt
from app.llm import analyse_incident
from app.report import build_report

 #Initialize the FastAPI app
app = FastAPI(
    title="DATA Quality Analyser",
    description= "Automatically generated RCA reports for data quality incidents using LLMs",
    version= "1.0.0"

)
# this defines what the incoming request body should look like 

class IncidentRequest(BaseModel):
    incident_id: str 

# load all incidents from Json once at startup 

with open("data/samples_logs.json","r") as f:
    ALL_INCIDENTS = json.load(f)

@app.get("/")
def root():
    """Health check - confirms the API is running"""
    return {"status": "Data Quality Analyser is running"}

@app.get("/incidents")
def list_incidents():
    """Returns all available incidents from the sample logs."""
    return {"incidents": ALL_INCIDENTS}

@app.post("/analyze")
def analyze(request: IncidentRequest):
    """
    Accepts an incident_id, finds the incident,
    runs it through the LLM, and returns a structured RCA report.
    """

    # Step 1: Find the incident by ID
    incident = next(
        (i for i in ALL_INCIDENTS if i["incident_id"] == request.incident_id),
        None
    )
    # If incident not found, return a 404 error
    if not incident:
        raise HTTPException(status_code=404, detail=f"{request.incident_id} not found")

    # Step 2: Build the prompt
    prompt = build_prompt(incident)

    # Step 3: Send to LLM and get response
    llm_response = analyse_incident(prompt)

    # Step 4: Build and return the final report
    report = build_report(incident, llm_response)

    return report
