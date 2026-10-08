#create a sample file to load
text = """Langchain is a framework for building AI apps.
It helps connect language models with your own data.
RAG means Retrival-Augmented Generation."""

with open("sample.txt", "w") as f:
    f.write(text)   
    print("Sample file created successfully.")

from langchain_community.document_loaders import TextLoader

loader = TextLoader("sample.txt")
documents = loader.load()

print("Number of Documents:", len(documents))
print("Content:")
print(documents[0].page_content)
