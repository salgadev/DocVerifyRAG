import os
import io
import argparse
import json
import openai
import sys
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.embeddings.fake import FakeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()


import io

def ingest(file_path):
    extension = os.path.splitext(file_path)[1].lower()

    if extension == '.pdf':
        loader = UnstructuredPDFLoader(file_path)
    elif extension == '.txt':
        loader = TextLoader(file_path)
    else:
        raise NotImplementedError('Only .txt or .pdf files are supported')

    # transform locally
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0,
    separators=[
        "\n\n",
        "\n",
        " ",
        ",",
        "\uff0c",  # Fullwidth comma
        "\u3001",  # Ideographic comma
        "\uff0e",  # Fullwidth full stop
        # "\u200B",  # Zero-width space (Asian languages)
        # "\u3002",  # Ideographic full stop (Asian languages)
        "",
    ])
    docs = text_splitter.split_documents(documents)

    return docs



def generate_metadata(docs):
    prompt_template = """
    BimDiscipline = ['plumbing', 'network', 'heating', 'electrical', 'ventilation', 'architecture']

    You are a helpful assistant that understands BIM documents and engineering disciplines. Your answer should be in JSON format and only include the filename, a short description, and the engineering discipline the document belongs to, distinguishing between {[d.value for d in BimDiscipline]} based on the given document."

    Analyze the provided document, which could be in either German or English. Extract the filename, its description, and infer the engineering discipline it belongs to. Document:
    context="
    """     
    # plain text     
    filepath = [doc.metadata for doc in docs][0]['source']
    context = "".join(
        [doc.page_content.replace('\n\n','').replace('..','') for doc in docs])

    prompt = f'{prompt_template}{context}"\nFilepath:{filepath}'

    #print(prompt)
    
    # Create client
    client = openai.OpenAI(
        base_url="https://api.together.xyz/v1",
        api_key=os.environ["TOGETHER_API_KEY"],
        #api_key=userdata.get('TOGETHER_API_KEY'),    
    )

    # Call the LLM with the JSON schema
    model_name = "mistralai/Mixtral-8x7B-Instruct-v0.1"
    chat_completion = client.chat.completions.create(
        model=model_name,        
        messages=[
            {
                "role": "system",
                "content": f"You are a helpful assistant that responsds in JSON format"                
            },
            {
                "role": "user",
                "content": prompt                                
            }
        ]
    )

    return json.loads(chat_completion.choices[0].message.content)    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate metadata for a BIM document")
    parser.add_argument("document", metavar="FILEPATH", type=str,
                        help="Path to the BIM document")

    args = parser.parse_args()

    if not os.path.exists(args.document) or not os.path.isfile(args.document):
        print("File '{}' not found or not accessible.".format(args.document))
        sys.exit(-1)

    docs = ingest(args.document)
    metadata = generate_metadata(docs)
    print(metadata)