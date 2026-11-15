from langchain_ollama import ChatOllama

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are are a friendly {subject} teacher. Expalin simply in unde 80 words, with one real-life example   "),
    ("user","{question}")
])


llm = ChatOllama(model="llama3.2:latest")
parser = StrOutputParser()


#LCEL (langchain Expression Language)
# chain = prompt_template | llm | parser

#chain = RunnableSequence(prompt_template, llm,parser)


#LCEL (langchain Expression Language)
chain = prompt_template | llm | parser

for chunk in chain.stream({"subject":"physics","question":"What is gravity"}):
    print(chunk,end="",flush=True)