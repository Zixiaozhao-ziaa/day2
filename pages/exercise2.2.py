import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
import numpy as np

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

st.title("Exercise 2.2 - Comparing Chunks")

text1 = st.text_area("Paste the first text")
text2 = st.text_area("Paste the second text")

if st.button("Compare"):
    if text1 and text2:
        # 生成embedding的函数
        def get_embedding(text):
            response = client.embeddings.create(
                input=text,
                model="text-embedding-3-large"
            )
            return response.data[0].embedding

        embedding1 = get_embedding(text1)
        embedding2 = get_embedding(text2)

        # 计算余弦相似度的函数
        def cosine_similarity(vec1, vec2):
            vec1 = np.array(vec1)
            vec2 = np.array(vec2)
            return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

        similarity = cosine_similarity(embedding1, embedding2)

        st.subheader("Result")
        st.write(f"Cosine similarity: {similarity:.4f}")
    else:
        st.warning("请把两段文字都填写完整")