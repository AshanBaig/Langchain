# jo summry and quiz bnaya tha wohi 
# 3_chain-->2_parallel_chain.py


from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser  # str means direct string ayegi .content kr ke nhi nikalna prga
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough


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
parser = StrOutputParser()
joke_gen_chain = RunnableSequence(prompt,model,parser)


prompt2 = PromptTemplate(
    template="Explain the following joke \n {joke}",
    input_variables=["joke"]
)
# passthrough = RunnablePassthrough()
# print(passthrough.invoke("jo bhi do wohi print"))
parallel_chain = RunnableParallel(
    {
        "joke":RunnablePassthrough() ,
        "Explanation": RunnableSequence(prompt2,model,parser)
    }
)

final_chain = RunnableSequence(joke_gen_chain , parallel_chain)
result  = final_chain.invoke({"topic": "I created netflix clone  "})
print(result)  # dict a rhi twet and linkdin is key 