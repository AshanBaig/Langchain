# workflow
"""
    1 feedback pr sentiments lain gye like pos or neg 
    if pos so pos reeply krdain gye like thanks for ur feedback etc
    if neg so we will reply can u share the detail , we will resolve it asap we will contact u personally etc.
    or negative pr customer servie ko email bhej de etc (ye sb agent krega abhi tw agent nhi ata bnana)
    
"""
    
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser  # str means direct string ayegi .content kr ke nhi nikalna prga
from langchain.schema.runnable import RunnableParallel,RunnableBranch,RunnableLambda
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field
from typing import Literal
GROQ_API_KEY = "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"

model = ChatOpenAI(
    api_key = GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",  # Groq OpenAI-compatible endpoint
    model="llama3-8b-8192"
)

parser = StrOutputParser()

class Feedback (BaseModel):
    sentiment : Literal["Positive","Negative"] =  Field (description="Give the sentiment of the feed back")

parser2 = PydanticOutputParser(pydantic_object=Feedback)
prompt1 = PromptTemplate(template = "Classify the sentiment of the following  text into postive or negative \n {feedback} \n {format_instruction}" ,
                        input_variables=["feedback"],
                        partial_variables={"format_instruction":parser2.get_format_instructions()})

classifier_chain = prompt1 | model | parser2

# result  =  classifier_chain.invoke({"feedback":"this is a terribl smartphone"})  # w hae to make sure ans hamesha consistent aye like positive or negative so we have to put literlal bcz next branch is pr depend kr rhi hy
# print(result.sentiment)

prompt2 = PromptTemplate (
    template="write an appropritae short response to this postive feedback just response nothing else  \n {feedback}",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate (
    template="write an appropritae short response to this negative feedback  jusr response nothing else  \n {feedback}",
    input_variables=["feedback"]
)
branch_chain = RunnableBranch(
    (lambda x : x.sentiment=="Positive",prompt2 | model | parser), # condition,chain
    (lambda x : x.sentiment=="Negative",prompt3 | model | parser),
    RunnableLambda(lambda  x : "could not find sentiments" )# ye chain nhi hy tw 
)
chain = classifier_chain | branch_chain
result = chain.invoke({"feedback": "this is the pretty annoying phone"})
print(result)

print(chain.get_graph().print_ascii())




