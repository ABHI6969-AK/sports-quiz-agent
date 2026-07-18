from src.database import populate_database, retrieve_context

populate_database()

facts = retrieve_context("Cricket history")

print(facts)
