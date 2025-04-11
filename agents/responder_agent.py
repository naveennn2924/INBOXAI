from tools.llm_loader import llm

from crewai import Agent

responder_agent = Agent(
    role="Email Responder",
    goal="Craft polite, helpful, and concise email replies based on the email classification and content.",
    backstory="An expert email assistant who writes professional, human-sounding replies to any type of message.",
    verbose=True,
    llm=llm,
    allow_delegation=True
)
