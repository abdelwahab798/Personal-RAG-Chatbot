import logging 
import os 
from config import Config
from langchain_classic.document_loaders import TextLoader, PDFMinerLoader
from langchain_classic.text_splitter import TokenTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

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


def Get_Data(file_path):
    try:
        if file_path in "txt":
            logger.info("File is txt file")
            loader=TextLoader(file_path=file_path)
            Doc=loader.load()
        
        else:
            loader=PDFMinerLoader(file_path)
            Doc=loader.load()
        logger.info("Extract data done")
    except Exception as e:
        logger.error("We have error in Get_Data:",e)
    
def Split_data(Doc):
    try:
        splitter=TokenTextSplitter(chunk_size=Config.chunk_size,chunk_overlap=Config.chunk_overlap)
        logger.info("Splitter is ready")
        chunks=splitter.split_documents(Doc)
    except Exception as e:
        logger.error("We have error in Split_data: ",e)

    

        
