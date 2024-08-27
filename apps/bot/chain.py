import os
import environ
from django.conf import settings

from langchain import hub
from langchain_openai import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# Initialize environment variables
env = environ.Env()
env.read_env(".env")

# Load documents
doc_path = os.path.join(settings.BASE_DIR, "chat_bot_database.txt")
data = TextLoader(doc_path)
docs = data.load()

# Split documents into smaller chunks
text_splitter = RecursiveCharacterTextSplitter()
text_splits = text_splitter.split_documents(docs)

# Initialize embeddings
embeddings = OpenAIEmbeddings(
    api_key=env("OPENAI_API_KEY"),
)

# Create a FAISS vector store from the split documents
vectorstore = FAISS.from_documents(text_splits, embeddings)
retriever = vectorstore.as_retriever()

# Define a function to format documents
format_docs = lambda docs: "\n\n".join(doc.page_content for doc in docs)

# Initialize LLM and other components
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.8,
)
# Pull RAG prompt from hub
rag_prompt = hub.pull("rlm/rag-prompt")

# Setup output parser
output_parser = StrOutputParser()


# Setup query processing
query = {
    "context": retriever | format_docs,
    "question": RunnablePassthrough(),
}

# Create and execute the chain
chain = query | rag_prompt | llm | output_parser
