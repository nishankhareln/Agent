from llama_index.core import StorageContext, load_index_from_storage
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core.query_engine.retriever_query_engine import RetrieverQueryEngine

def extract_structured_resume(persist_dir="./vector_db"):
    storage_context = StorageContext.from_defaults(
        vector_store=ChromaVectorStore(persist_dir=persist_dir)
    )
    index = load_index_from_storage(storage_context)
    query_engine = RetrieverQueryEngine.from_index(index)

    query = (
        "Extract structured resume information: "
        "name, email, phone, skills, education, experience. "
        "Format output in JSON."
    )
    response = query_engine.query(query)
    
    # Safely return the parsed result
    return response.response  # or response.get_response() or .to_dict(), depending on version
