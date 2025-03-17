import argparse
import fitz
import os
import json
from langchain_ollama import OllamaLLM
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain

parser = argparse.ArgumentParser(prog='RAG: LLM for doing conversation from data present in a file.')
parser.add_argument("--path", "-p", default="./data_registry/data.pdf")
args = parser.parse_args()
FILE_PATH = args.path


def extract_text_from_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = "\n".join(page.get_text("text") for page in doc)
    return text

def extract_text_from_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return json.dumps(data, indent=2)  # Convert JSON to formatted text

def extract_text_from_code(file_path):
    """Extract text from code files (.py, .cpp, .java)"""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()  # Treat as plain text

def extract_text(file_path):
    """Detect file type and extract text accordingly."""
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()
    if file_extension in [".txt", ".md"]:
        return extract_text_from_txt(file_path)
    elif file_extension == ".pdf":
        return extract_text_from_pdf(file_path)
    elif file_extension == ".json":
        return extract_text_from_json(file_path)
    elif file_extension in [".py", ".cpp", ".java"]:
        return extract_text_from_code(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")


def get_file_retriever(filename):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    text_data = extract_text(filename)
    docs = text_splitter.create_documents([text_data])
    # vector Store
    embedding_model = OllamaEmbeddings(model="all-minilm")
    vectorstore = FAISS.from_documents(docs, embedding_model)
    # retriever
    retriever = vectorstore.as_retriever()
    return retriever

# Initialize LLM and retriever
llm = OllamaLLM(model="gemma3:1b", base_url="http://localhost:11434")
retriever = get_file_retriever(FILE_PATH)
conversation_chain = ConversationalRetrievalChain.from_llm(llm, retriever=retriever)

def launch_tui():
    print("Data Repository used: "+FILE_PATH)
    query = ""
    chat_history = []  # Store previous interactions
    while query != "/quit":
        query = input("Ask me anything! (Type /quit to exit) >>> ")
        response = conversation_chain.invoke({"question": query, "chat_history": chat_history})
        # Store conversation history
        chat_history.append((query, response["answer"]))
        print(">>> "+response["answer"])

launch_tui()