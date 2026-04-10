from langchain_openai import ChatOpenAI
from config.settings import LLM_BASE_URL, LLM_MODEL

def writer_agent(query: str, context: str):
    llm = ChatOpenAI(
        base_url=LLM_BASE_URL,
        model=LLM_MODEL,
        temperature=0.3,
        api_key="lm-studio"
    )

    prompt = f"""
You are an AI Research Assistant.

Your task is to write a SHORT and clear research report.

⚠️ IMPORTANT:
- Topic is STRICTLY: "{query}"
- Do NOT change the topic
- Do NOT introduce any other topic
- Keep the answer concise and relevant

Structure:
1. Introduction
2. Key Points
3. Conclusion

Start with:
Research Report: {query}

Use this research data:
{context}
"""

    response = llm.invoke(prompt)
    return response.content