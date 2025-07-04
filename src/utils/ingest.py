from langchain_community.vectorstores import FAISS
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from euriai.langchain_embed import EuriaiEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def generate_vector_store(pdf_path):
    loader = PyMuPDFLoader(pdf_path)
    pages = loader.load()
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(pages)
    embeddings = EuriaiEmbeddings(api_key=API_KEY)
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local("vector_store")
