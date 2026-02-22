from datetime import datetime


def build_report(incident: dict, llm_response: str) -> dict:
    """
    Takes the original incident and the LLM's raw text response
    and returns a clean structured report as a dictionary.
    """

    report = {
        "report_generated_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "incident_id": incident["incident_id"],
        "pipeline": incident["pipeline"],
        "error_type": incident["error_type"],
        "severity": incident["severity"],
        "timestamp": incident["timestamp"],
        "rca_analysis": llm_response
    }

    return report
