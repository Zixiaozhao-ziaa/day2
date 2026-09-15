import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import numpy as np

load_dotenv()

st.title("exercise 2.4")

#set up a vector database

#Exercise 2.3 - Implementing RAG Manually

#In Exercise 2.1, you wrote some code to chunk a document into composite parts.

#In Exercise 2.2, you wrote some code to compare two blocks of text.

#Combine and extend these pieces of code to create an application that does the following things:

#1.Allows the user to ask questions of the document from Exercise 2.1.

#2.Retrieves the most relevant part of the document and uses this to answer the question.

#3.Responds to the user, citing what information was used from the document.