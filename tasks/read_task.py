from crewai import Task
from agents.reader_agent import reader_agent

read_task = Task(
    description="Fetch unread emails from inbox and extract basic fields.",
    expected_output="A list of email objects with subject, sender, and body.",
    agent=reader_agent
)
