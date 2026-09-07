import os

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

documents=[]

folder="data"

for file in os.listdir(folder):

    path=os.path.join(folder,file)

    with open(path,"r",encoding="utf-8") as f:

        text=f.read()

    documents.append(
        Document(
            page_content=text,
            metadata={"source":file}
        )
    )

splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks=splitter.split_documents(documents)

embeddings=GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

db=FAISS.from_documents(
    chunks,
    embeddings
)

db.save_local("vectorstore")

print("Vector DB Created Successfully")