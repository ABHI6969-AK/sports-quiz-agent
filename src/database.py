import json
import chromadb

from src.config import CHROMA_DB_PATH, SPORTS_DATA_PATH

# Create ChromaDB client
client = chromadb.PersistentClient(path=CHROMA_DB_PATH)

# Create or get collection
collection = client.get_or_create_collection(
    name="sports_collection"
)


def load_data():
    """
    Load sports facts from JSON file.
    """
    with open(SPORTS_DATA_PATH, "r") as file:
        return json.load(file)


def populate_database():
    """
    Insert sports facts into ChromaDB.
    Runs only if database is empty.
    """
    existing = collection.count()

    if existing > 0:
        print("✅ Database already populated.")
        return

    data = load_data()

    for idx, item in enumerate(data):
        collection.add(
            documents=[item["fact"]],
            metadatas=[{"sport": item["sport"]}],
            ids=[str(idx)]
        )

    print("✅ ChromaDB populated successfully!")


def retrieve_context(query, n_results=5):
    """
    Retrieve relevant facts from ChromaDB.
    """
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    return results["documents"][0]