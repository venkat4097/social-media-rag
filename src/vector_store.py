# src/vector_store.py

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# In-memory FAISS index (for 384-d embeddings from MiniLM)
dimension = 384
faiss_index = faiss.IndexFlatL2(dimension)

# Store original tweets for retrieval
tweet_store = []

def embed_and_store(tweets):
    global tweet_store

    # Embed all tweets
    embeddings = embedder.encode(tweets, convert_to_numpy=True)

    # Add to FAISS index
    faiss_index.add(embeddings)
    tweet_store.extend(tweets)

    return "Embedding and storing complete"

def query_tweets(query):
    query_embedding = embedder.encode([query], convert_to_numpy=True)
    distances, indices = faiss_index.search(query_embedding, k=5)

    results = []
    for idx in indices[0]:
        if idx < len(tweet_store):
            results.append(tweet_store[idx])

    return results if results else ["No matching tweets found."]
