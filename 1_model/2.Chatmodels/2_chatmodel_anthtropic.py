from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()

model = ChatAnthropic(model="claude") # api ky nhi hy
result = model.invoke("What is apple")
print(result)