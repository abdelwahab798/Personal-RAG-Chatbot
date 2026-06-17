from config import Config
from langchain_community.document_loaders import TextLoader, PyPDFLoader,json_loader
from langchain_text_splitters import TokenTextSplitter
from logger_config import get_logger
import requests
from langchain_core.documents import Document
logger = get_logger("load_split")

def Get_Data(file_path=None):
    try:
        if file_path is None:
            return None
        if file_path.endswith(".txt"):
            logger.info("File is txt file")
            loader=TextLoader(file_path=file_path)
            Doc=loader.load()
        elif file_path.endswith(".pdf"):
            loader=PyPDFLoader(file_path)
            Doc=loader.load()
        elif file_path.startswith("https"):
            logger.info("user enter linked profile")
            payload = {
                    "q": file_path,
                    "gl": "eg",
                    "hl": "en"}
            headers = {
                'X-API-KEY': Config.API_KEY2,
                'Content-Type': 'application/json'}
            response = requests.request("POST", Config.url, headers=headers, json=payload)
            data = response.json()
            logger.info("data scraped done")
            linkedin_text=""
            if "organic" in data and len(data["organic"])>0:
                for result in data["organic"]:
                    title = result.get("title", "")
                    snippet = result.get("snippet", "")
                    linkedin_text += f"Title: {title}\nDetails: {snippet}\n\n"
                    logger.info("data is done and save in varible")
            else:
                logger.info("system can't scraping data")
                linkedin_text="we didn't have any inforamtions"
            Doc = [Document(page_content=linkedin_text, metadata={"source": "LinkedIn_Scraper"})]
        else:
            logger.info("user dose't enter data")
            Doc=None
        return Doc
    except Exception as e:
        logger.error("We have error in Get_Data:",e)
    
def Split_data(Doc):
    try:
        if Doc is None:
            logger.info("we dose't have data to split")
            return []
        else:
            splitter=TokenTextSplitter(chunk_size=Config.chunk_size,chunk_overlap=Config.chunk_overlap)
            logger.info("Splitter is ready")
            chunks=splitter.split_documents(Doc)
            logger.info("Split data is done")
            return chunks
    except Exception as e:
        logger.error("We have error in Split_data: ",e)
        return []
        
        
        

    

        
