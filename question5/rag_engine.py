import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_community.vectorstores import FAISS

load_dotenv()

embeddings=GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

db=FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

llm=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

def get_answer(query):

    docs=db.similarity_search(query,k=4)

    context="\n\n".join([
        doc.page_content
        for doc in docs
    ])

    sources=list(set([
        doc.metadata["source"]
        for doc in docs
    ]))

    prompt=f"""
You are an Insurance Copilot.

Answer ONLY from the context.

If not found say:
'Not available in policy documents'

Context:
{context}

Question:
{query}

Provide:
1. Answer
2. Coverage Details
3. Source
"""

    response=llm.invoke(prompt)

    return {
        "answer":response.content,
        "sources":sources
    }