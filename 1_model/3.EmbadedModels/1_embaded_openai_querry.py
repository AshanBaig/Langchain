from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embading =  OpenAIEmbeddings(model="text-embedding-3-large",dimensions= 50)   # 50 dimension ka vector ayega 
result = embading.embed_query("Hello My name Is Ashan Baig")
print(result) # vector print ho rha hoga 
