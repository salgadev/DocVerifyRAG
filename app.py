import streamlit as st
import io
import tempfile

from scripts import generate_metadata, ingest


st.title('PDF to Text Converter')
st.write('This app converts a PDF file to plain text.')

uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf","txt"])

if uploaded_file is not None:
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp:
            tmp.write(uploaded_file.read())
            file_path = tmp.name

        docs = ingest(file_path)
        metadata = generate_metadata(docs)
        st.write('## Converted Text')
        st.write(metadata)

        # Clean up the temporary file
        os.remove(file_path)

    except Exception as e:
        st.error(f'Error: {e}')