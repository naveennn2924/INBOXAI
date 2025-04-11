from crewai import Crew
from tasks.classify_task import get_classify_task
from tasks.escalate_task import get_escalate_task
from tasks.respond_task import get_respond_task
from tools.vector_store import MemoryManager

from agents.classifier_agent import classifier_agent
from agents.escalator_agent import escalation_agent
from agents.responder_agent import responder_agent

memory = MemoryManager()

def email_response_flow(email):
   
    classify_task = get_classify_task(email["subject"], email["body"])
    classification = Crew(
        agents=[classifier_agent],
        tasks=[classify_task]
    ).kickoff()

    
    escalate_task = get_escalate_task(email["subject"], email["body"], classification)
    escalation = Crew(
        agents=[escalation_agent],
        tasks=[escalate_task]
    ).kickoff()

    if escalation == "Escalate to Human":
        return {
            "from": email["from"],
            "subject": email["subject"],
            "body": email["body"],
            "classification": classification,
            "reply": "Escalated to human",
            "escalated": True
        }

  
    similar = memory.search_similar(email["subject"], email["body"])
    memory_context = "\n\n".join([f"[Similar #{i+1}]\n{doc.page_content}" for i, doc in enumerate(similar)])

    
    respond_task = get_respond_task(email["subject"], email["body"], classification, memory_context)
    reply = Crew(
        agents=[responder_agent],
        tasks=[respond_task]
    ).kickoff()

    
    memory.add_memory(email["subject"], email["body"], classification, reply)

    return {
        "from": email["from"],
        "subject": email["subject"],
        "body": email["body"],
        "classification": classification,
        "reply": reply,
        "escalated": False
    }
