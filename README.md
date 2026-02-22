# Data Quality Analyser

An AI-powered automation system that analyzes production data quality incidents and automatically generates structured Root Cause Analysis (RCA) reports using a local LLM.

## What it does

Instead of an engineer manually reading through incident logs and writing an RCA document, this tool does it in seconds.

You send an incident ID → the system finds the incident → builds a structured prompt → runs it through an LLM → returns a clean RCA report with root cause, impact analysis, and remediation actions.

## Tech Stack

- **FastAPI** — REST API framework
- **Ollama (llama3.2)** — Local LLM for incident analysis
- **Pydantic** — Request/response validation
- **Python** — Core language

## Project Structure

```
data_quality_analyser/
├── app/
│   ├── main.py        # FastAPI app and endpoints
│   ├── prompt.py      # Prompt engineering logic
│   ├── llm.py         # LLM connection (Ollama)
│   └── report.py      # Report generation
├── data/
│   └── sample_logs.json   # Simulated production incident logs
├── reports/               # Generated RCA reports
├── .env                   # API keys (not committed)
└── requirements.txt
```

## Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/your-username/data_quality_analyser.git
cd data_quality_analyser
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Ollama and pull the model
```bash
# Download Ollama from https://ollama.com
ollama pull llama3.2
ollama serve
```

### 4. Start the API
```bash
uvicorn app.main:app --reload
```

### 5. Open the interactive docs
```
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/incidents` | List all incidents |
| POST | `/analyze` | Generate RCA report for an incident |

## Example

**Request:**
```json
{
  "incident_id": "INC-001"
}
```

**Response:**
```json
{
  "report_generated_at": "2024-01-03 08:30:00 UTC",
  "incident_id": "INC-001",
  "pipeline": "customer_orders_etl",
  "error_type": "NullValueError",
  "severity": "HIGH",
  "rca_analysis": "1. ROOT CAUSE: ... 2. IMPACT ANALYSIS: ... 3. REMEDIATION ACTIONS: ..."
}
```

## Incident Types Covered

- **NullValueError** — Null values in non-nullable columns
- **SchemaMismatch** — Wrong data types in pipeline
- **LateArrivingData** — Events arriving past SLA window

## Key Design Decisions

- Prompt engineering is isolated in `prompt.py` so it can be improved independently
- LLM connection is isolated in `llm.py` so the model can be swapped without touching other files
- Uses local LLM (Ollama) — no API costs, no data sent externally
