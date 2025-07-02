
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from pydantic import BaseModel,Field
from langchain_core.output_parsers import StrOutputParser  # str means direct string ayegi .content kr ke nhi nikalna prga
load_dotenv()

GROQ_API_KEY = "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"

model = ChatOpenAI(
    api_key = GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",  # Groq OpenAI-compatible endpoint
    model="llama3-8b-8192"
)
# flow 1 topic pr kch likhwae gye then usko 5 line me convert krain gye

template1 = PromptTemplate(template="Give summary of {topic}",
                           input_variables=["topic"])
template2 = PromptTemplate(template="convert these following text into 5 lines not more than that {text}",
                           input_variables=["text"])

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser  # chain bna di
result = chain.invoke({"topic":"black hole"})
print(result)
print(chain.get_graph().print_ascii())