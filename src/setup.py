from config import Config
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain_core.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from logger_config import get_logger
logger = get_logger("Setup")



def define_llm():
    try:
        llm =ChatOpenAI(api_key=Config.API_key, base_url=Config.base_url,model=Config.model,temperature=Config.temperature)
        logger.info("define llm is done")
        chat=ConversationChain(llm=llm,memory=ConversationBufferMemory())
        logger.info("chat is ready")
        return chat
    except Exception as e:
        logger.error("we have error in define_llm in setup.py: ",e)
    
def system_prompt(query,VectroDB):
    try:
        temp=""" you are assistant, Answer the next Question using provided context,
        ## context :
        {context}
        ## Question :
        {Question}"""
        temp=PromptTemplate.from_template(temp)
        query=query
        simlir=VectroDB.similarity_search_with_score(query,k=3)
        context=[]
        for i in simlir:
            context.append(i[0].page_content)
        prompt=temp.format(context="\n".join(context),Question=query)
        logger.info("prompt system is done")
        return prompt
    except Exception as e:
        logger.info("we have error in system_prompt in setup.py: ",e)



    
