from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"
    )

model = ChatHuggingFace(llm=llm)

# flow 1 topic pr kch likhwae gye then usko 5 line me convert krain gye

template1 = PromptTemplate(template="Give summary of {topic}",input_variables=["topic"])

template2 = PromptTemplate(template="convert these following text into 5 lines not more than that {text}",input_variables=["text"])

prompt1 =  template1.invoke({"topic":"Black hole"})


result1 = model.invoke(prompt1)
# print(result1)
prompt2 =  template2.invoke({"text":result1.content})

result2 = model.invoke(prompt2)
print(result2.content)