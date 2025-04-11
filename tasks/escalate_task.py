from agents.escalator_agent import escalation_agent
from crewai import Task

def get_escalate_task(subject, body, classification):
    return Task(
        description="Determine if this email needs human escalation based on classification and content.",
        expected_output="'Escalate to Human' or 'No Escalation Needed'",
        agent=escalation_agent 
    )
