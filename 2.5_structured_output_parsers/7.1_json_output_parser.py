# open ai pr tight chlega 
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser  # str means direct string ayegi .content kr ke nhi nikalna prga
load_dotenv()

GROQ_API_KEY = "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"

model = ChatOpenAI(
    api_key = GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",  # Groq OpenAI-compatible endpoint
    model="llama3-8b-8192"
)





parser = JsonOutputParser()
# flow 1 topic pr kch likhwae gye then usko 5 line me convert krain gye

template = PromptTemplate(template="""
You are an API backend. Your response MUST be a valid JSON object. Do not include explanations, text, or markdown. Only raw JSON.

Expected JSON Structure:
{format_instruction}

Question:
Give me the name, age, and country of a famous cricketer.
""",
                           input_variables=[],
                           partial_variables={"format_instruction":parser.get_format_instructions()}) # partial varible user nhi btata khud a kr fill ho jata




# prompt = template.format()  
# result = model.invoke(prompt)
# print("Result Content",result.content)
# final_result = parser.parse(result.content)  # parse krna prega 
# print("Final_result ",final_result)
# print("type: ",type(final_result))




# chain bhi bna skhe hain 
chain = template |model |parser
result = chain.invoke({}) # koe input varible nhi hy but humain bhjna hy tw empty dict is best
print(result)


# problem isme hum schema enforce nhi kr skhte like json object me agr hum 5 fruits mang rhy tw 
# ho skhta 1 key ho fruit or 5 fruit hn list me but we want fruit1 pehla fruit fruit2 dosra fruit