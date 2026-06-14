from config import Config
import logging
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from logger_config import get_logger
logger = get_logger("Embedding")


def embedding_data(chunks):
    try:
        embeddings=HuggingFaceEmbeddings(
        model_name=Config.embedding_model,
        model_kwargs={"device":"cpu"})
        logger.info("embedding model is ready")
        vectors=embeddings.embed_documents(i.page_content for i in chunks)
        return vectors,embeddings
    except Exception as e:
        logger.error("we have errro in embedding_data: ",e)

def create_Vector_DB(chunks,embeddings):
    try:
        vector_DB=FAISS.from_documents(chunks,embeddings)
        logger.info("VectroDB is created")
        return vector_DB
    except Exception as e:
        logger.error("we have error in create_Vector_DB: ",e)





