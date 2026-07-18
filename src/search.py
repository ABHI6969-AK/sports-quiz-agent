from duckduckgo_search import DDGS


def search_web(query):
    """
    Search the web for recent sports information.
    Returns top 3 results.
    """
    results = []

    with DDGS() as ddgs:
        for item in ddgs.text(query, max_results=3):
            results.append(item["body"])

    return results