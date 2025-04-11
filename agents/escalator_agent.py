from crewai import Agent
from tools.llm_loader import llm

escalation_agent = Agent(
    role="Escalation Handler",
    goal="Decide whether an email requires manual review or automatic reply",
    backstory="Acts like an experienced human assistant who knows when not to trust automation.",
    verbose=True,
    llm=llm,
    allow_delegation=True
)
