from config import Config
import logging
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from logger_config import get_logger
logger = get_logger("Embedding")


def embedding_data():
    try:
        embeddings=HuggingFaceEmbeddings(
        model_name=Config.embedding_model,
        model_kwargs={"device":"cpu"})
        logger.info("embedding model is ready")
        return embeddings
    except Exception as e:
        logger.error("we have errro in embedding_data: ",e)



def vector_DB_mange(chunks=None,mode=None):
    try:
        embeddings=embedding_data()
        logger.info("load embeddings is done")
        if not embeddings:
            return None
        
        if mode in ["create","add",None] and (chunks is None or len(chunks)==0):
            logger.info(f"we can't do {mode} with no data we switch mode to ""load"" ")
            mode="load"
        
        if mode=="create":
            logger.info("user select create")
            vector_DB=FAISS.from_documents(chunks,embeddings)
            logger.info("DB is created")
            vector_DB.save_local(Config.DB_path)
            logger.info(f"DB is save in:  {Config.DB_path}")
            return vector_DB

        elif mode=="load":
            vector_DB=FAISS.load_local(Config.DB_path,embeddings,allow_dangerous_deserialization=True)
            logger.info("DB is loaded")
            if not vector_DB:
                logger.info("we didn't have any inforamtions")
                return None
            return vector_DB
        
        elif mode=="add":
            vector_DB=FAISS.load_local(Config.DB_path,embeddings,allow_dangerous_deserialization=True)
            logger.info("DB is loaded")
            if not vector_DB:
                logger.info("we didn't have any inforamtions")
                return None
            vector_DB.add_documents(chunks)
            logger.info("new inforamtions is added")
            vector_DB.save_local(Config.DB_path)
            logger.info(f"DB is save in:  {Config.DB_path}")
            return vector_DB
    except Exception as e:
        logger.error("we have error in vector_DB_mange")






    






