from agents.classifier_agent import classifier_agent
from crewai import Task

def get_classify_task(subject, body):
    return Task(
        description="Classify the email into categories: 'Meeting Request', 'Support Inquiry', 'Newsletter', 'Job Offer', 'Spam', or 'Other'.",
        expected_output="'Meeting Request', 'Support Inquiry', 'Newsletter', 'Job Offer', 'Spam', or 'Other'.",
        agent=classifier_agent 
    )
