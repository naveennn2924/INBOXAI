from crewai import LLM


llm = LLM(
    model="openai/gpt-4o-mini", 
    temperature=0.8,
    max_tokens=150,
    top_p=0.9,
    frequency_penalty=0.1,
    presence_penalty=0.1,
    stop=["END"],
    seed=42
)
