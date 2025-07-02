from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.output_parsers import  StructuredOutputParser,ResponseSchema # str means direct string ayegi .content kr ke nhi nikalna prga
load_dotenv()

GROQ_API_KEY = "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"

model = ChatOpenAI(
    api_key = GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",  # Groq OpenAI-compatible endpoint
    model="llama3-8b-8192"
)

schema = [
    ResponseSchema(name="fact1",description="fact 1 about the topic"),
    ResponseSchema(name="fact2",description="fact 2 about the topic"),
    ResponseSchema(name="fact3",description="fact 3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

# model tyar hy parser bhi tyar hy ab me apna prompt bnauga

template  = PromptTemplate(template="Tell me only three facts about {topic} \n {format_instruction}",
                           input_variables=["topic"],
                           partial_variables={"format_instruction":parser.get_format_instructions()}
                           )
""" agr chain na bnau tw mujhy pehle teplate se prompt banna prega by giving input varibles,
    phr us prompt ko model me bhej kr mujhy ans lena hy then parser.parse krna hy for structured output
"""


chain = template | model | parser 
result  = chain.invoke({"topic":"black hole"})
for i in result:
    print(i," : ",result[i])
