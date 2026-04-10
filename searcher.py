from tavily import TavilyClient

tavily = TavilyClient(api_key="your_api_key_here")

def search_agent(plan: str):
    queries = []

    # 🔹 Plan ko line by line break karo
    for line in plan.split("\n"):
        if line.strip() != "" and len(line) < 200:
            queries.append(line.strip())

    all_results = ""

    # 🔹 Har query pe search chalao
    for q in queries[:3]:  # max 3 queries
        try:
            res = tavily.search(query=q, max_results=2)
            for r in res["results"]:
                all_results += r["content"] + "\n\n"
        except:
            continue

    return all_results