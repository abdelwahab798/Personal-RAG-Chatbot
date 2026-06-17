from setup import define_llm,system_prompt
from load_split import Get_Data,Split_data
from Embedding import embedding_data, vector_DB_mange

def main():
    mode=input("please enter your mode in this options : load , create , add : ")
    Data=None
    if mode in ["create","add"]:
        Data=input("please enter your resources such as txt file , pdf or LinkedIn profile link: ")
    
    Doc=Get_Data(Data)
    chunks=Split_data(Doc)
    vector_DB=vector_DB_mange(chunks,mode=mode)
    chat=define_llm()
    while True:
        prompt=input("please enter your question if you want to off please enter ""off"": ")
        if prompt.lower() == "off":
            break
        if not prompt:
            continue
        try:
            prompt=system_prompt(prompt,vector_DB)
            response=chat.run(prompt)
            print("answer: ",response)
            print("-" * 50)
        except Exception as e:
            print("Error")


if __name__ == "__main__":
    main()


