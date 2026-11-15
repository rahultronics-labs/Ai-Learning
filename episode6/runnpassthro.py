from langchain_ollama import ChatOllama

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough



llm = ChatOllama(model="llama3.2:latest")

parser = StrOutputParser()

question_prompt_template = ChatPromptTemplate.from_template("explain in simple 3 lines: \n {question}") | llm | parser
rate_prompt_template = ChatPromptTemplate.from_template(
    "Question: {question} \nAnswer: {answer} \n" \
    "Rate how clear the answer is for a 15-year-old student on a scale of 1 to 10, " \
    "where 1 is very unclear and 10 is very clear. with one line of feedback."
)


explain_chain =  question_prompt_template | llm | parser



#print(explain_chain.invoke({"question": "What is the capital of France?"}))

feedback_chain = RunnablePassthrough.assign(answer = explain_chain) | rate_prompt_template | llm | parser

print(feedback_chain.invoke({"question": "What is capital of France"}))