from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.1,
        "max_new_tokens": 50
    }
)

model = ChatHuggingFace(llm=llm)

messages = [
    # SystemMessage(content="You are a helpful assitant please be huble and kind "),
    HumanMessage(content="Where is my refund of order #12345")
]
result = model.invoke(messages)

messages.append(AIMessage(content = result.content.split("<|assistant|>")[1]))
print(messages[0].content)