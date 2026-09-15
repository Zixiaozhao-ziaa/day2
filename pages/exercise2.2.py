import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


st.title("Exercise2.2")

#allow the user to copy and paste two different texts
if "Text_1" not in st.session_state:
    st.session_state.text_1 = ""

if "Text_2" not in st.session_state:
    st.session_state.text_2 = ""

st.session_state.text_1 = st.text_area(
    label="Text 1"
)

st.session_state.text_2 = st.text_area(
    label="Text 2"
)

## create an embedding for each chunck of text. For this you willneed to use the embedding function from the 
client = OpenAI()

response = client.embeddings. create(
    input="Your text string goes here", model="text-embedding-3-large"
)

print(response.data[0].embedding)

##display