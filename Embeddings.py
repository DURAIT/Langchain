from langchain_openai import OpenAIEmbeddings, embeddings
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


# A small, cheap, high-quality OpenAI embedding model
embeddings = OpenAIEmbeddings(model="text-embedding-3-small", api_key = api_key)

print("OpenAI embedding model is ready!")

text = "I want to learn AI and Python"
vector = embeddings.embed_query(text)
#print("Vector:", vector)
print("Vector 5 elements:", vector[:5])

import numpy as np

def similarity(a, b):
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

v1 = embeddings.embed_query("I like dogs")
v2 = embeddings.embed_query("I love puppies")
v3 = embeddings.embed_query("The car is fast")

print("dogs vs puppies (similar):", round(similarity(v1, v2), 2))
print("dogs vs car   (different):", round(similarity(v1, v3), 2))
print("puppies vs car(different):", round(similarity(v2, v3), 2))


