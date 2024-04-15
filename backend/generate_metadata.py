import os

import argparse
import json
import openai

from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.embeddings.fake import FakeEmbeddings
from langchain_community.vectorstores import Vectara

from schema import Metadata, BimDiscipline

load_dotenv()

vectara_customer_id = os.environ['VECTARA_CUSTOMER_ID']
vectara_corpus_id = os.environ['VECTARA_CORPUS_ID']
vectara_api_key = os.environ['VECTARA_API_KEY']

vectorstore = Vectara(vectara_customer_id=vectara_customer_id,
                      vectara_corpus_id=vectara_corpus_id,
                      vectara_api_key=vectara_api_key)


def ingest(file_path):
    extension = filepath.split('.')[-1]
    ext = extension.lower()
    if ext == 'pdf':
        loader = UnstructuredPDFLoader(file_path)
    elif ext == 'txt':
        loader = TextLoader(file_path)

    # transform locally
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    vectara = Vectara.from_documents(docs, embedding=FakeEmbeddings(size=768))    
    retriever = vectara.as_retriever()

    return retriever


def extract_metadata(filename):
    with open(filename, 'r') as f:
        context = f.readlines()

    # Create client
    client = openai.OpenAI(
        base_url="https://api.together.xyz/v1",
        api_key=os.environ["TOGETHER_API_KEY"],
    )

    # Call the LLM with the JSON schema
    chat_completion = client.chat.completions.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        response_format={"type": "json_object", "schema": Metadata.model_json_schema()},
        messages=[
            {
                "role": "system",
                "content": f"You are a helpful assistant that understands BIM documents and engineering disciplines. Your answer should be in JSON format and only include the title, a brief one-sentence summary, and the discipline the document belongs to, distinguishing between {[d.value for d in BimDiscipline]} based on the given document."
            },
            {
                "role": "user",
                "content": f"Analyze the provided document, which could be in either German or English. Extract the title, summarize it briefly in one sentence, and infer the discipline. Document:\n{' '.join(context)}"
            }
        ]
    )

    created_user = json.loads(chat_completion.choices[0].message.content)
    return created_user

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate metadata for a BIM document")
    parser.add_argument("document", metavar="FILEPATH", type=str,
                        help="Path to the BIM document")

    args = parser.parse_args()

    if not os.path.exists(args.document) or not os.path.isfile(args.document):
        print("File '{}' not found or not accessible.".format(args.document))
        sys.exit(-1)

    metadata = extract_metadata(args.document)
    print(json.dumps(metadata, indent=2))