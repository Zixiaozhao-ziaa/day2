import streamlit as st
from PyPDF2 import PdfReader
import os

st.title("Exercise 2.1")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # 用 PyPDF2 解析 PDF,提取文字
    reader = PdfReader(uploaded_file)
    string_data = ""
    for page in reader.pages:
        string_data += page.extract_text() or ""

    st.subheader("Chunk the document")
    chunk_size = st.number_input(
        "Select chunk size (characters)",
        min_value=100,
        max_value=2000,
        value=500,
        step=100
    )

    def chunk_text(text, size):
        return [text[i:i + size] for i in range(0, len(text), size)]

    chunks = chunk_text(string_data, chunk_size)
    st.write(f"Document split into {len(chunks)} chunks.")

     # ------------------------------------------------------
    # 3. Save each chunk to your project directory
    # ------------------------------------------------------
    output_dir = "chunks"
    os.makedirs(output_dir, exist_ok=True)

    for i, chunk in enumerate(chunks):
        file_path = os.path.join(output_dir, f"chunk_{i+1}.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(chunk)

    st.success(f"Saved {len(chunks)} chunks to the '{output_dir}' directory.")

    first_chunk_path = os.path.join(output_dir, "chunk_1.txt")
    with open(first_chunk_path, "r", encoding="utf-8") as f:
        first_chunk = f.read()

# ------------------------------------------------------
# 5. Display the first chunk back to the user
# ------------------------------------------------------
    st.subheader("First chunk")
    if st.button("Show first chunk"):
        st.write(first_chunk)