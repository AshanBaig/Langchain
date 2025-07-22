# jo summry and quiz bnaya tha wohi 
# 3_chain-->2_parallel_chain.py


from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser  # str means direct string ayegi .content kr ke nhi nikalna prga
from langchain.schema.runnable import RunnableSequence,RunnableParallel

from langchain_openai import ChatOpenAI

GROQ_API_KEY = "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"

model = ChatOpenAI(
    api_key = GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",  # Groq OpenAI-compatible endpoint
    model="llama3-8b-8192"
)

prompt1 = PromptTemplate(
    template= "Crate a Linkdinn post about \n{topic}",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template= "Craete a Tweeter post about \n {topic}",
    input_variables=["topic"]
)
parser = StrOutputParser()
parallel_chain = RunnableParallel(
    {
        "tweet":RunnableSequence(prompt2,model,parser),
        "linkdin": RunnableSequence(prompt1,model,parser)
    }
)
result  = parallel_chain.invoke({"topic": "I created netflix clone  "})
print(result)  # dict a rhi twet and linkdin is key 