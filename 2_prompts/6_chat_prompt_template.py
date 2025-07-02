from langchain_core.prompts import ChatPromptTemplate

# chat_template = ChatPromptTemplate([
#     SystemMessage (content="you are a helpful {domain} exprt"),
#     HumanMessage(content="Explain in simple terms and in roman urdu , what is {topic}")
# ])

# alternate
chat_template = ChatPromptTemplate([
    # tuple bhejdo 
    ("system","you are a helpful {domain} exprt"),
    ("human","Explain in simple terms and in roman urdu , what is {topic}")
])

prompt = chat_template.invoke({
    "domain":"Cricket Expert",
    "topic": "dusra"
})
print(prompt) #HumanMessage(content='Explain in simple terms and in roman urdu , what is {topic} aise print ho rha hy place holder nhi a rha so use alternate way