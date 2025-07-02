from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser  # str means direct string ayegi .content kr ke nhi nikalna prga
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"
    )

model = ChatHuggingFace(llm=llm)

# flow 1 topic pr kch likhwae gye then usko 5 line me convert krain gye

template1 = PromptTemplate(template="Give summary of {topic}",
                           input_variables=["topic"])
template2 = PromptTemplate(template="convert these following text into 5 lines not more than that {text}",
                           input_variables=["text"])

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser  # chain bna di
result = chain.invoke({"topic":"black hole"})
print(result)