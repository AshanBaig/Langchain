
from langchain_core.prompts import PromptTemplate
template = PromptTemplate(template="""Please summarize the research paper titled {paper_input} with the following

specifications:

Explanation Style: {style_input}

Explanation Length: {length_input}

1. Rathematical Details:

Include relevant mathematical equations if present in the paper.

Explain the mathematical concepts using simple, intuitive code snippets where applicable.

2. Analogies:

Use relatable analogies to simplify complex ideas.

If certain information is not available in the paper, respond with: "Insufficient Information available" instead of gessing.

Ensure the sumary is clear, acurate, and aligned with the provided style and length""",input_variables=["paper_input","style_input","length_input"],validate_template=True)
# validation means agr koe input varible me chez dena bhol gye tw hath ke hath error   
template.save("template.json")  # agr koe or page bhi mera same prompt use krna chahe tw araam se kr skhta hy