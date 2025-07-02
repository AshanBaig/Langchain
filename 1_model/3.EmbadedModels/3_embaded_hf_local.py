from langchain_huggingface import HuggingFaceEmbeddings

embading = HuggingFaceEmbeddings(model ="sentence-transformers/all-MiniLM-L6-v2")

text = "I am from karachi am"

document = [
    "Hi my name is Ashan",
    "I am from karachi",
    "This is document"
]
result = embading.embed_query(document)
print(result)