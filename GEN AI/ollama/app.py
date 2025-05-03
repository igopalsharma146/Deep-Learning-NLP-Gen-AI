import os 
from dotenv import load_dotenv
# from langchain_community.llms import Ollama

from langchain_ollama import OllamaLLM
# from langchain.llms import O
import streamlit as st 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

##prompt template 
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant.Please respond to the question"),
        ("human", "{question}"),
    ]
)

##streamlit framework 
st.title("LangChain Chatbot")
question = st.text_input("Ask a question:")

##ollama model 
llm = OllamaLLM(model ="llama2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if question:
    st.write(chain.invoke({"question": question}) )