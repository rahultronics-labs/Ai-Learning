import ollama

messages = [
    {"role": "system", "content": "behave like bengaluru auto driver.in one line answer"},{
        "role": "user", "content": "What is ai"
    }]

model_name = "llama3.2:latest"

response = ollama.chat(model = model_name, messages = messages)

print(response.message.content)