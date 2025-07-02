from langchain_huggingface import HuggingFaceEndpoint
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
st.header("Research tool")

user_input = st.text_input("Enter your Querry")
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"
    )
if st.button("Summarize"):
    result = llm.invoke(user_input)
    st.text(result)
    print(result)