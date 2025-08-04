from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

client = chromadb.Client()
collection = client.get_or_create_collection("tweets")

embedder = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

def embed_and_store(tweets):
    documents = [{"id": str(i), "document": tweet} for i, tweet in enumerate(tweets)]
    for doc in documents:
        collection.add(documents=[doc["document"]], ids=[doc["id"]])
    return "Embedding and storing complete"

def query_tweets(query):
    results = collection.query(query_texts=[query], n_results=5)
    return results["documents"][0] if results["documents"] else []
