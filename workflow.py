import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langgraph.graph import StateGraph
from typing import TypedDict

from agents.planner import planner_agent
from agents.searcher import search_agent
from agents.writer import writer_agent

# 🧠 State define karte hain
class GraphState(TypedDict):
    query: str
    plan: str
    search: str
    report: str

# 🔹 Step 1: Planner Node
def plan_node(state: GraphState):
    plan = planner_agent(state["query"])
    return {"plan": plan}

# 🔹 Step 2: Search Node
def search_node(state: GraphState):
    results = search_agent(state["plan"])
    return {"search": results}

# 🔹 Step 3: Writer Node (🔥 FIX HERE)
def writer_node(state: GraphState):
    report = writer_agent(state["query"], state["search"])  # ✅ FIXED
    return {"report": report}

# 🧩 Build Graph
builder = StateGraph(GraphState)

builder.add_node("planner", plan_node)
builder.add_node("search", search_node)
builder.add_node("writer", writer_node)

# 🔗 Flow define karo
builder.set_entry_point("planner")
builder.add_edge("planner", "search")
builder.add_edge("search", "writer")

# 🚀 Compile graph
app = builder.compile()

# ▶️ Test run
if __name__ == "__main__":
    result = app.invoke({
        "query": "Impact of AI in Healthcare"
    })

    print("\nFINAL OUTPUT:\n")
    print(result["report"])