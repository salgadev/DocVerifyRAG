from langchain_community.document_loaders import UnstructuredPDFLoader

def ingest_pdf(path):
    loader = UnstructuredPDFLoader()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

    return data