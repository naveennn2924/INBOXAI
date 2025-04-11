from agents.responder_agent import responder_agent
from crewai import Task

def get_respond_task(subject, body, classification, memory_context):
    return Task(
        description="Generate a professional email reply based on the classification, body, and memory context.",
        expected_output="A complete email reply in a professional tone.",
        agent=responder_agent  
    )
