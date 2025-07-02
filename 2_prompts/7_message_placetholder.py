from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

# chat template
chat_template =ChatPromptTemplate([
    ("system","You are a helpful customer support agent"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human","{query}")  # query puchne se pehle hum load history krain gye
])


# load histroy 
chat_history =[]
# text file se load krain gye simple
with open("chat_history.txt") as f:
    for i in f.readlines():
        chat_history.append(i)

print(chat_history)
# create prompt
prompt = chat_template.invoke({"chat_history":chat_history,"query":"Where is my refund "})
print (prompt)