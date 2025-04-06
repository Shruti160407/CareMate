import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader #VSI creates a searchable vector index for the document which we have uploaded and SDR is use to load and read the documents from the directory 
from llama_index.llms.openai import OpenAI as LlamaOpenAI # for qurrying the index data

llama_llm = LlamaOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY")) #it initializes openai gpt-3.5 model

documents = SimpleDirectoryReader("data").load_data()

index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine(llm = llama_llm)

def query_documents(user_query: str) -> str:
    return str(query_engine.query(user_query))