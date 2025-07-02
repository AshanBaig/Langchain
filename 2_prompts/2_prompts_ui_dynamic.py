from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate,load_prompt
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

st.header("Research tool")
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"
    )

# select box
paper_options = {
    "Attention Is All You Need": {
        "authors": "Vaswani et al.",
        "source": "NeurIPS 2017"
    },
    "BERT: Pre-training of Deep Bidirectional Transformers for Language": {
        "authors": "Devlin et al.",
        "source": "NAACL 2019"
    },
    "AlphaFold: Predicting Protein Structures with Deep Learning": {
        "authors": "DeepMind (Jumper et al.)",
        "source": "Nature 2021"
    },
    "Diffusion Models Beat GANs on Image Synthesis": {
        "authors": "Dhariwal and Nichol",
        "source": "NeurIPS 2021"
    },
    "Chain-of-Thought Prompting Elicits Reasoning in LLMs": {
        "authors": "Wei et al.",
        "source": "arXiv 2022"
    }
}

# 2. Explanation styles
styles = [
    "Beginner-Friendly",
    "Mathematical",
    "Code-Based",
    "Visual/Diagrammatic",
    "Conceptual Breakdown"
]

# 3. Explanation lengths
lengths = ["Short (~1-2 paragraphs)", "Medium (~4-5 paragraphs)", "Long (Full breakdown)"]

# UI
st.title("🧠 Research Paper Explainer Generator")

paper_input = st.selectbox("📄 Select a Research Paper", list(paper_options.keys()))
style_input = st.selectbox("🎯 Choose Explanation Style", styles)
length_input = st.selectbox("📏 Choose Explanation Length", lengths)

# now template

template = load_prompt("template.json")
# fille the place holder for chain comment
# prompt = template.invoke(
#     {
#         "paper_input": paper_input,
#         "style_input":style_input,
#         "length_input":length_input
#     }
# )

### Why didnt we use f string (
#     reuseable hy
#     hum tempalte alag file ka bna kr json se import kr skhte hain
#     Langchain Ecosystem me araam s fit ho jata hy lik chain bnane me etc



# if st.button("Summarize"):
#     result = llm.invoke(prompt)
#     print(result)
#     st.text(result)

# Agr chain bnana hy tw 2bar invoke nhi krna prega
if st.button("Summarize"):
    chain = template | llm
    result = chain.invoke({
        "paper_input": paper_input,
        "style_input":style_input,
        "length_input":length_input
    })
    print(result)
    st.text(result)