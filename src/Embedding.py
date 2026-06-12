from langchain_community.embeddings import HuggingFaceEmbeddings
import logging 
import os 
from config import Config

log_dir="logs"
os.makedirs(log_dir,exist_ok=True)

logger=logging.getLogger("data_ingestion")
logger.setLevel("DEBUG")

consle_handler=logging.StreamHandler()
consle_handler.setLevel("DEBUG")

log_file_path=os.path.join(log_dir,"Project.log")
file_handler=logging.FileHandler(log_file_path)
file_handler.setLevel("DEBUG")

formater=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
consle_handler.setFormatter(formater)
file_handler.setFormatter(formater)

logger.addHandler(consle_handler)
logger.addHandler(file_handler)

def embedding_data(chunks):
    try:
        embeddings=HuggingFaceEmbeddings(
            model_name=Config.embedding_model,
            model_kwargs={"device":"cpu"})
        logger.info("embedding model is ready")
        vectors=embeddings.embed_documents(i.page_content for i in chunks)