from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embading =  OpenAIEmbeddings(model="text-embedding-3-large",dimensions= 50)   # 50 dimension ka vector ayega 

document = [
    "Hi my name is Ashan",
    "I am from karachi",
    "This is document"
]

result = embading.embed_documents(document )
print(result) # vector print ho rha hoga 
