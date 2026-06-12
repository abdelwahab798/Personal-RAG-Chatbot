import os 
from dotenv import load_dotenv
load_dotenv()

class Config():
    API_key=os.getenv("API_key")
    base_url=os.getenv("base_url")
    model=os.getenv("model")
    temperature=float(os.getenv("temperature"))
    chunk_size=float(os.getenv("chunk_size"))
    chunk_overlap=float(os.getenv("chunk_overlap"))
    embedding_model=os.getenv("embedding_model")
