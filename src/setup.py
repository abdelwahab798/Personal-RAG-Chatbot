from langchain_openai import ChatOpenAI
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

def define_llm():
    try:
        llm = ChatOpenAI(
    api_key=Config.API_key,
    base_url=Config.base_url,
    model=Config.model,
    temperature=Config.temperature)
        logger.info("define llm is done")
    except Exception as e:
        logger.error("we have error in define llm: ",e)
    
