from langchain_ollama import ChatOllama
from pydantic import BaseModel , Field

llm = ChatOllama(model = "llama3.2:latest")

#problem


text = "hey, I'm rahul, I'm 24 years old, you can reach me at rahulpjogur948@gmail.com "

#response = llm.invoke(f"Extract user's name,age and email id from the text: {text}")

#print(type(response.content))

class UserDetails(BaseModel):
    name: str = Field(description = "Complete Name")
    age: int = Field(description = "User's Age")
    email: str = Field(description = "Useer Email")

structured_llm = llm.with_structured_output(UserDetails)

response = structured_llm.invoke(f"Extraxt user's name, age and email id from the text: {text}")

#print(response.name)
#print(response.age)

dis_output = response.model_dump()
print(dis_output)
