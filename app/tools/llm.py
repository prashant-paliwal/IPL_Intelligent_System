from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from litellm import completion, embedding


MODEL = "gpt-4o-mini"

def call_llm(prompt: str) -> str:
    response = completion(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    return response["choices"][0]["message"]["content"]

def get_embedding(text: str):
    res = embedding(
        model="text-embedding-3-small",
        input=text
    )
    return res["data"][0]["embedding"]