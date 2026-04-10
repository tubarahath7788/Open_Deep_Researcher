import os
from dotenv import load_dotenv

load_dotenv()

LLM_BASE_URL = "http://localhost:1234/v1"
LLM_MODEL = "qwen2.5-7b-instruct-1m"

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")