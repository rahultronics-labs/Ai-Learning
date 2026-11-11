from langchain_ollama import ChatOllama

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are are a friendly AI assistant. Answer clearly and simply."),
    ("placeholder", "{messages}")
])





llm = ChatOllama(model = "llama3.2:latest")

parser =StrOutputParser()

chain = prompt_template | llm | parser

messages = []

while True:
    user = input("You: ")
    if user == "bye":
        break
    

    user_role = ({"role":"user","content":user})
    messages.append(user_role)

    print("Assistant:", end="", flush=True)

    response = ""

    for chunk in chain.stream({"messages": messages}):
        
        print(chunk, end="", flush=True)

        response += chunk
    print()
    assistant_role = {"role":"assistant", "content":response}   
    messages.append(assistant_role)