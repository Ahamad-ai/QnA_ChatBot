import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv
load_dotenv()

## Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "QnA Chatbot with OPENAI"
os.environ["LANGSMITH_ENDPOINT"]="https://api.smith.langchain.com"

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant and please response to the user queryies"),
        ("user","Question: {question}"),
    ]
)

def generate_response(question,api_key,llm,temperature,max_tokens):
    """Generate a response from the LLM."""
    openai.api_key = api_key
    llm = ChatOpenAI(
        model_name=llm,
        openai_api_key=api_key,
        temperature=temperature,
        max_tokens=max_tokens

    )
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer=chain.invoke({"question":question})
    return answer


### Title of the app
st.title("Q and A Chatbot with OpenAI")

## Sidebar for settings
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter your Open AI API Key:",type="password")

## Drop down to select various Open AI models

llm = st.sidebar.selectbox("Select an Open AI Model",["gpt-4.1","gpt-4o",""])

## Adjust response parameter
temperature = st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens",min_value=50,max_value=300,value=150)

## Main Interface for user input
st.write("Hey! nice to meet you , ask me any question")
user_input=st.text_input("You:")

if user_input:
    response=generate_response(user_input,api_key,llm,temperature,max_tokens)
    st.write(response)

else:
    st.write("Please write a query")


