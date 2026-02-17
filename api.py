from fastapi import FastAPI
from pydantic import BaseModel

from llama_index.core import Settings, VectorStoreIndex, StorageContext, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.chroma import ChromaVectorStore

app = FastAPI()

class QueryReq(BaseModel):
    question: str

# 起動時に一度だけ作って使い回す
Settings.embed_model = HuggingFaceEmbedding("BAAI/bge-small-en-v1.5")
Settings.llm = Ollama(model="llama3:instruct", system_prompt="あなたは日本語でのみ回答するアシスタントです。必ず日本語で回答してください。")

docs = SimpleDirectoryReader("./docs").load_data()
vector_store = ChromaVectorStore.from_params(
    collection_name="rag-demo",
    persist_dir="./chroma_db",
)
index = VectorStoreIndex.from_documents(
    docs,
    storage_context=StorageContext.from_defaults(vector_store=vector_store),
)
query_engine = index.as_query_engine()

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/query")
def query(req: QueryReq):
    resp = query_engine.query(req.question)
    return {"answer": str(resp)}
