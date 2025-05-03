from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os 
from langserve import add_routes
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="Gemma2-9b-It",groq_api_key= groq_api_key)

##create prompt templatee 
system_template= "Translate the following into {language}"
prompt_template = ChatPromptTemplate.from_messages(
  [
      ("system" , system_template), ("user" , "{text}")
  ]  
)

##create output parser 
output_parser = StrOutputParser()

