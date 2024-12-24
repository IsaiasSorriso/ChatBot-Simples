from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Aqui é o histórico da conversa: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model 

def chat():
    context = ""
    print("Bem vindo ao Chat, digite 'sair' para sair")
    while True:
        user_input =input("Você: ")
        if user_input.lower() == "sair":
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("Bot: ", result)
        context += f"\nVocê: {user_input}\nBot: {result}\n"

if __name__ == "__main__":
    chat()
