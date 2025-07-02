# Working
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.1,
        "max_new_tokens": 100
    }
)

model = ChatHuggingFace(llm=llm)
# use normal chat_history list wla  code for correct output dont use system smg wla code  duplicate item just to understand how meassages work but OPEN AI nhi tw that's why we dont prefer system smg wla code 

chat_history = ["focus on last question and if u dont understand full context so see 2nd last and if u can find answer so find if not so see 3rd last and so on"]
# chat_history = [
#     SystemMessage(content=" focus on last human message  and if u dont understand full context so see 2nd last and if u can find answer so find if not so see 3rd last and so on"),
# ]
while True:
    
    user_input = input("You: ")
    if user_input =="quit":
        break
    chat_history.append(user_input)
    # chat_history.append(HumanMessage(content=user_input))
    result = model.invoke(chat_history)
    chat_history.append(result.content.split("<|assistant|>")[1])
    # chat_history.append(AIMessage(content=result.content.split("<|assistant|>")[1]))
    print(f"AI: {result.content.split("<|assistant|>")[1]}")
    
print(chat_history)
# ab ye nhi pta konsa msg kisne bheja tha like konsa user ka tha konsa AI kax