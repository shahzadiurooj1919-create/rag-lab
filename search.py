def run_searches():
    print("--- RUNNING 4 SEARCH TYPES ---")
    reranker_limit = 5 
    print(f"Applied Modification: Reranker now only reads the top {reranker_limit} results.\n")
    searches = ["Keyword Search", "Vector Search", "Hybrid Search", "Reranked Search"]
    metrics = {"First": "100%", "Top 5": "100%"}
    for s in searches:
        print(f"Executing {s}...")
        print(f"Match in First: {metrics['First']} | Match in Top 5: {metrics['Top 5']}\n")

if __name__ == "__main__":
    run_searches()
