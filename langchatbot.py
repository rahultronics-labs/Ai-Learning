from langchain_ollama import ChatOllama

model_name = "llama3.2:latest"

messages = [
    {"role":"system", "content":"you are a helpful assistant."
     , "model": model_name}
]

while True:
    user = input("You: ")
    if user == "bye":
        break
    user_role = ({"role":"user","content":user})

    messages.append(user_role)

    llm = ChatOllama(model = model_name, messages = messages)
    response = llm.invoke(messages)
    response = response.content
    print("Assistant:", response)

    assitant_role = {"role":"assitant", "content":response}
