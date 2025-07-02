from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
chatmodel = ChatOpenAI(model="gpt-3.5-turbo")
result = chatmodel.invoke("What is the capital of sindh")
print(result) 