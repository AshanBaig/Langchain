# kisi bhi python function ko execute krna ho  in chain (runnable bna kr) tw we use it  

# working --> 1 joke generate krain gye and joke ke sath sath we want to print no. of words in that joke 


from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser  # str means direct string ayegi .content kr ke nhi nikalna prga
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda


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


joke_gen_chain = RunnableSequence(prompt, model,parser)

def word_counter(text):
    return len(text.split())

runnable_word_counter = RunnableLambda(word_counter)  # lambdafunc bhi likh skhte direct    RunnableLambda(lambda x : len(x.split()))


parallel_chain  = RunnableParallel({
    "joke" : RunnablePassthrough(),
    "length" : runnable_word_counter
})


final_chain = RunnableSequence(joke_gen_chain,parallel_chain)
result =  final_chain.invoke({"topic":"exams sucks"})

print(result)