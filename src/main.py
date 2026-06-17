from setup import define_llm,system_prompt
from load_split import Get_Data,Split_data
from Embedding import embedding_data, vector_DB_mange
from config import Config

chat=define_llm()
Doc=Get_Data()
chunks=Split_data(Doc)
embeddings=embedding_data()
vector_DB=vector_DB_mange(chunks,mode="load")
prompt=system_prompt(Config.prompt,vector_DB)

response=chat.run(prompt)
print(response)



