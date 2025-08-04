import streamlit as st
from src.ingestion import fetch_tweets
from src.trend_detect import extract_keywords
from src.vector_store import embed_and_store, query_tweets
from src.generator import generate_answer
import os
from dotenv import load_dotenv
import nltk
nltk.download('stopwords')
nltk.download('punkt')  # if you're using tokenizers
load_dotenv()

st.title("🔥 Social Media RAG - Trending Topics")

query = st.text_input("Enter a topic or hashtag (e.g., #AI, cricket):")

if st.button("Fetch & Analyze") and query:
    try:
        bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
        tweets = fetch_tweets(bearer_token, query)
        st.success(f"Fetched {len(tweets)} tweets.")

        keywords = extract_keywords(tweets)
        st.subheader("🔍 Trending Keywords")
        for word, count in keywords:
            st.write(f"{word} — {count} times")

        embed_and_store(tweets)
        st.success("Tweets embedded and stored in vector DB.")

        st.subheader("🗨️ Sample Tweets")
        for tweet in tweets[:5]:
            st.write("📌", tweet)

    except Exception as e:
        st.error(f"❌ {str(e)}")

st.subheader("💬 Ask something based on tweets:")
user_query = st.text_input("Your question (e.g., What's trending in AI?)")

if user_query:
    retrieved = query_tweets(user_query)
    st.write("🧠 Most relevant tweets:")
    for tweet in retrieved:
        st.write("🔹", tweet)

    response = generate_answer(user_query, retrieved)
    st.subheader("🧾 Context-Aware Response:")
    st.write(response)
