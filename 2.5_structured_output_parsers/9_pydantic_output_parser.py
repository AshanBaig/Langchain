# model se 1 person ka data laingye jo json format me hoga or name agre city laingye age lazmi int hogi


from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser  # str means direct string ayegi .content kr ke nhi nikalna prga
load_dotenv()

GROQ_API_KEY = "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"

model = ChatOpenAI(
    api_key = GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",  # Groq OpenAI-compatible endpoint
    model="llama3-8b-8192"
)

class Person(BaseModel):
    name : str = Field(description="name of the person")
    age : int = Field (gt=18, description="age of the person")
    city : str = Field (description="name of the city person belongs to")
    
parser =  PydanticOutputParser(pydantic_object=Person)  # schema bta dia data validation khud kr lega

tempalte = PromptTemplate(
    template = "Generate the name age city of the fictional character {place} person \n {format_instruction}", # place asi dal dia hy hy like pakisai person etc
    input_variables = ["place"], 
    partial_variables= {"format_instruction":parser.get_format_instructions()}
)

chain = tempalte | model | parser
result = chain.invoke({"place": "pakistani"})
print(result)
    
    


