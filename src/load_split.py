from config import Config
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import TokenTextSplitter
from logger_config import get_logger
logger = get_logger("load_split")

def Get_Data(file_path):
    try:
        if file_path.endswith(".txt"):
            logger.info("File is txt file")
            loader=TextLoader(file_path=file_path)
            Doc=loader.load()
        else:
            loader=PyPDFLoader(file_path)
            Doc=loader.load()
        logger.info("Extract data done")
        return Doc
    except Exception as e:
        logger.error("We have error in Get_Data:",e)
    
def Split_data(Doc):
    try:
        splitter=TokenTextSplitter(chunk_size=Config.chunk_size,chunk_overlap=Config.chunk_overlap)
        logger.info("Splitter is ready")
        chunks=splitter.split_documents(Doc)
        logger.info("Split data is done")
        return chunks
    except Exception as e:
        logger.error("We have error in Split_data: ",e)
        return []
        
        

    

        
