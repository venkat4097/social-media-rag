# Social Media Trend Analysis with RAG

This Streamlit app identifies trending topics from social media (Twitter) and provides contextual answers using Retrieval-Augmented Generation (RAG) with OpenAI.

---

## 🔗 Deployment Link
https://social-media-rag-3zxwaappspdphxypcu9xq7j.streamlit.app/

---

## 🛠️ Setup & Run Instructions

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/social-media-rag.git
cd social-media-rag

## 🔗 Summary

The project is a Social Media Trend Analysis Tool using Retrieval-Augmented Generation (RAG). It fetches trending tweets, extracts keywords, stores embeddings in a vector store, and answers user queries using OpenAI.

Key components:

Tweet Ingestion: Tweets are fetched using the Twitter API with keyword-based search or mocked for fallback.

Trend Detection: Uses nltk and RAKE for keyword extraction to identify trending phrases/topics.

Vector Store: Embeds tweets using SentenceTransformer and stores them in a ChromaDB in-memory vector store.

Query & Retrieval: A user query is embedded and matched against stored vectors to retrieve relevant tweets.

Answer Generation (RAG): The most relevant tweets are passed as context to OpenAI to generate a meaningful, contextual answer.

User Interface: Streamlit is used for a clean UI to input queries, show trends, and display responses.



---
