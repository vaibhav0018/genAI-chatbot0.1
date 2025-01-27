import pandas as pd
from io import StringIO
import requests
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.docstore.document import Document
from app.config import Config

documents = []
vectorstore = None

def fetch_google_sheet_data():
    global documents, vectorstore
    response = requests.get(Config.GOOGLE_SHEET_URL)
    response.raise_for_status()

    csv_data = StringIO(response.text)
    custom_data = pd.read_csv(csv_data)

    # Create documents for each entry
    documents = [Document(page_content=f"Q: {row['Question']} A: {row['Answer']}") 
                for index, row in custom_data.iterrows()]

    # Load documents into Chroma vector store
    embedding_function = HuggingFaceEmbeddings(
        model_name='sentence-transformers/all-MiniLM-L6-v2'
    )
    vectorstore = Chroma.from_documents(documents, embedding=embedding_function)

def get_documents():
    return documents

def get_vectorstore():
    return vectorstore






