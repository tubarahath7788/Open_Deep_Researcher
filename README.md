# 🤖 AI Research Assistant (Open Deep Researcher)

An AI-powered research assistant built using a multi-agent architecture that automates the process of researching and generating structured reports.

## 🚀 Features

- 🔹 Multi-Agent System (Planner, Search, Writer)
- 🔹 Automated Research Workflow
- 🔹 Real-time Web Search (Tavily API)
- 🔹 Structured Report Generation using LLM
- 🔹 Streamlit UI for user interaction
- 🔹 LangGraph-based workflow orchestration

## 🧠 Architecture

User Input → Planner Agent → Search Agent → Writer Agent → Final Report

## ⚙️ Tech Stack

- Python
- LangChain
- LangGraph
- Streamlit
- Tavily API
- LM Studio / OpenAI-compatible LLM

## 📊 Workflow

1. Planner breaks query into sub-questions  
2. Search agent fetches relevant data  
3. Writer agent generates final report  
4. Output displayed in UI  

## 🖥️ How to Run

```bash
# Clone repo
git clone https://github.com/tubarahath7788/open-deep-researcher.git

# Go to folder
cd open-deep-researcher

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Streamlit UI
streamlit run ui/app.py
