import streamlit as st
import io
import tempfile

from scripts import generate_metadata, ingest


st.title('PDF to Text Converter')
st.write('This app converts a PDF file to plain text.')

uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf","txt"])

if uploaded_file is not None:
    try:
        file_ext = uploaded_file.name.split('.')[-1].lower()
        pdf_file = io.BytesIO(uploaded_file.read())
        docs = ingest(pdf_file, file_ext)
        metadata = generate_metadata(docs)
        st.write('## Converted Text')
        st.write(metadata)
    except Exception as e:
        st.error(f'Error: {e}')