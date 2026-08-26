import numpy as np
import sys 
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

FILE_NAME = sys.argv[1] if len(sys.argv) > 1 else print("Please provide a file name as a command line argument.") or sys.exit(1)

if not os.path.exists(FILE_NAME):
    raise FileNotFoundError(f"Could not find '{FILE_NAME}' in your current VS Code directory.")

with open(FILE_NAME, "r") as file:
    raw_text = file.read()

embeddings_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=600,
    chunk_overlap=100,
    separators=["\n\n", "\n", " ", ""]
)

docs = text_splitter.create_documents([raw_text])
texts = [doc.page_content for doc in docs]
vectors = embeddings_model.embed_documents(texts)

def cosine_similarity(vec_a, vec_b):
    dot_product = np.dot(vec_a, vec_b)
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    return dot_product / (norm_a * norm_b) if norm_a and norm_b else 0.0

num_vectors = len(vectors)
similarity_matrix = np.zeros((num_vectors, num_vectors))

for i in range(num_vectors):
    for j in range(num_vectors):
        similarity_matrix[i][j] = cosine_similarity(vectors[i], vectors[j])

query = input("Enter search query: ")
query_vector = embeddings_model.embed_query(query)
similarities = [cosine_similarity(query_vector, vec) for vec in vectors]
for similarity in [sorted(similarities)[:5]]:
    print(f"Similarity: {similarity:.2f}, Text: {text[:100]}...")