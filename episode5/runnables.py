from langchain_ollama import ChatOllama

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutParser

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are are a friendly {subject} teacher. Expalin simply in unde 80 words, with one real-life example   "),
    ("user","{question}")
])



prompt = prompt_template.invoke({"subject":"math", "question": "What is the pythagorean theorem?"})

print(prompt)
model_name = "llama3.2:latest"

llm = ChatOllama(model = model_name)

response = llm.invoke(prompt)

parser =StrOutputParser()

response = parser.invoke(response)

print(response.content)