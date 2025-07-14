import os
from llama_cloud import GeminiEmbeddingConfig
from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core.schema import Document
from typing import List
import google.generativeai as genai

embedding = GeminiEmbeddingConfig(api_key="AIzaSyBZ3mmxdgsIXQ-FfdEkrwVGCKFQfgk0lvw")

class GeminiEmbedding:
    def __init__(self, model_name="models/embedding-001", api_key=None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not set")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name)

    def get_text_embedding(self, text: str) -> List[float]:
        response = self.model.embed_content(content=text)
        return response["embedding"]

    def get_text_embeddings(self, texts: List[str]) -> List[List[float]]:
        return [self.get_text_embedding(t) for t in texts]


def create_vector_index(text: str, persist_dir="./vector_db"):
    documents = [Document(text=text)]
    embedding = GeminiEmbedding(api_key="your_gemini_api_key_here")  # Set directly
    vector_store = ChromaVectorStore(persist_dir=persist_dir)

    index = VectorStoreIndex.from_documents(
        documents,
        embedding=embedding,
        vector_store=vector_store
    )
    index.storage_context.persist(persist_dir)
    return index
