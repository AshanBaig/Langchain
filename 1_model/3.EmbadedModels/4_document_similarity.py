from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


embading = HuggingFaceEmbeddings(model ="sentence-transformers/all-MiniLM-L6-v2")


document = [
    "Babar Azam khan – A stylish Pakistani batter known for his consistency and elegant strokeplay.",
    "Virat Kohli – An aggressive Indian run-machine and modern legend in all formats.",
    "Ben Stokes – England’s fearless all-rounder, famous for clutch performances under pressure.",
    "Rashid Khan – Afghanistan’s star leg-spinner who dominates T20 leagues worldwide.",
    "MS Dhoni – India’s coolest captain and finisher, known for his calm mind and sharp tactics."
]
query =  "give me spinner"

doc_emb = embading.embed_documents(document)
query_emb =  embading.embed_query(query)

score = cosine_similarity([query_emb],doc_emb)[0]  # 2d list leta hy

score_ind = list(enumerate(score))
result = sorted(score_ind,key=lambda x: x[1],reverse=True)

print(document[result[0][0]])