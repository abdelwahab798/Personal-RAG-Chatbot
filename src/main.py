from setup import define_llm,system_prompt
from load_split import Get_Data,Split_data
from Embedding import embedding_data, create_Vector_DB
from config import Config

chat=define_llm()
Doc=Get_Data("https://www.linkedin.com/in/abdelwahab-amr-a168892a3")
chunks=Split_data(Doc)
vectors,embeddings=embedding_data(chunks)
vector_DB=create_Vector_DB(chunks,embeddings)
prompt=system_prompt(Config.prompt,vector_DB)

response=chat.run(prompt)
print(response)



