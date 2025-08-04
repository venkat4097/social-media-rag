import requests
import json
import os
def fetch_tweets(bearer_token, query, max_results=50):
    url = "https://api.twitter.com/2/tweets/search/recent"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    params = {
        "query": query,
        "max_results": max_results,
        "tweet.fields": "text",
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(f"Error fetching tweets: {response.text}")

    data = response.json()
    return [tweet["text"] for tweet in data.get("data", [])]


# def fetch_tweets():
#     # Temporarily load from local mock file
#     mock_file_path = os.path.join("data", "mock_tweets.json")
#     with open(mock_file_path, "r", encoding="utf-8") as f:
#         tweets = json.load(f)
#     return tweets