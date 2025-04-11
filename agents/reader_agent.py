from crewai import Agent
from tools.llm_loader import llm




reader_agent = Agent(
    role="Email Reader",
    goal="Fetch unread emails and extract subject, sender, and content",
    backstory="Expert in handling email protocols and parsing messages.",
    llm=llm,  
    verbose=True,
    allow_delegation=True
)

