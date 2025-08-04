import os
from dotenv import load_dotenv
load_dotenv()  # Add this here too
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def generate_answer(question, context_docs):
    context = "\n".join(context_docs)
    prompt = f"""You are a social media expert.
Based on the following tweets:
{context}

Answer the question: {question}"""

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content.strip()
