def build_prompt(incident: dict) -> str:
    """
    Takes a single incident log (as a dictionary) and builds
    a structured prompt to send to the LLM.
    """

    prompt = f"""
You are a senior data engineer analyzing a production data quality incident.

Below is the incident log:

- Incident ID     : {incident['incident_id']}
- Timestamp       : {incident['timestamp']}
- Pipeline        : {incident['pipeline']}
- Error Type      : {incident['error_type']}
- Affected Table  : {incident['affected_table']}
- Affected Columns: {', '.join(incident['affected_columns'])}
- Error Message   : {incident['error_message']}
- Severity        : {incident['severity']}

Based on the above, provide a structured Root Cause Analysis (RCA) report with exactly these three sections:

1. ROOT CAUSE
   Explain why this error likely occurred.

2. IMPACT ANALYSIS
   Explain what systems, teams, or processes are affected and how seriously.

3. REMEDIATION ACTIONS
   List clear, actionable steps to fix the issue and prevent recurrence.

Be concise, technical, and precise.
"""
    return prompt.strip()