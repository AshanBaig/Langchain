from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser  # str means direct string ayegi .content kr ke nhi nikalna prga
from langchain.schema.runnable import RunnableSequence


GROQ_API_KEY = "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"

model = ChatOpenAI(
    api_key = GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",  # Groq OpenAI-compatible endpoint
    model="llama3-8b-8192"
)

prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)


prompt2 = PromptTemplate(
    template="Explain the following joke \n {joke}",
    input_variables=["joke"]
)

parser = StrOutputParser()

chain = RunnableSequence(prompt,model,parser,prompt2,model,parser)

result = chain.invoke({"topic":"CS Enginner"})
print(result)