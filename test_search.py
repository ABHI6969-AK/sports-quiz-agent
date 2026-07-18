from src.search import search_web

results = search_web("Latest Cricket World Cup news")

for result in results:
    print(result)
    print("-" * 50)