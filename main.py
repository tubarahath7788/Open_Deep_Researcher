from agents.planner import planner_agent
from agents.searcher import search_agent
from agents.writer import writer_agent

query = "Impact of AI in healthcare"

# Step 1: Plan
plan = planner_agent(query)
print("PLAN:\n", plan)

# Step 2: Extract questions
questions = [q for q in plan.split("\n") if "?" in q][:2]

# Step 3: Search (LIMIT DATA 🔥)
all_results = []

for q in questions:
    result = search_agent(q)
    
    # limit length to avoid token error
    short_result = result[:500]
    
    all_results.append(short_result)

search_results = "\n\n".join(all_results)

print("\nSEARCH RESULTS:\n", search_results)

# Step 4: Final report
final_report = writer_agent(search_results)

print("\nFINAL REPORT:\n", final_report)