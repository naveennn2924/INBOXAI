from crewai import Agent
from tools.llm_loader import llm
classifier_agent = Agent(
    role="Email Classifier",
    goal="Categorize emails into types like support, meeting, newsletter, spam, or job inquiry.",
    backstory="An expert email assistant trained on tons of inboxes. Can identify intent and urgency in emails with ease.",
    verbose=True,
    llm=llm,
    allow_delegation=True
)
