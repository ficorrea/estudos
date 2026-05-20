import os
os.environ["LANGGRAPH_STRICT_MSGPACK"] = "True"

from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages # -> gera uma estrutura de mensagens para o estado
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama
from collections.abc import Sequence

# Conecta ao Ollama
llm = ChatOllama(model="llama3.2:1b")

class Estado(TypedDict):
    messages: Annotated[list, add_messages]

# Chama a LLM e adiciona a resposta ao estado
def responder(estado: Estado):
    resposta = llm.invoke(estado["messages"])
    return {"messages": [resposta]}

builder = StateGraph(Estado)
builder.add_node("responder", responder)
builder.add_edge(START, "responder")
builder.add_edge("responder", END)
graph = builder.compile()

# if __name__ == "__main__":
#     # Fluxo 1
#     # Esse fluxo não tem memória, só mensagens recentes são enviadas. 
#     while True:
#         user_input = input("Questão: ")
        
#         if user_input.lower() in ["q", "quit"]:
#             print("Encerrando o programa.")
#             break

#         resposta = graph.invoke({"messages": [{"role": "user", "content": user_input}]})
#         print("AI:", resposta["messages"][-1].content)

if __name__ == "__main__":
    # Fluxo 2
    # Esse fluxo mantém um histórico de mensagens, ou seja, 
    # todas as mensagens anteriores são enviadas para a LLM.
    current_messages: Sequence[BaseMessage] = []

    while True:
        user_input = input("Questão: ")
        
        if user_input.lower() in ["q", "quit"]:
            print("Encerrando o programa.")
            break
        
        human = HumanMessage(content=user_input)
        current_messages = [*current_messages, human]

        resposta = graph.invoke({"messages": current_messages})
        current_messages = resposta["messages"]
        
        print("AI:", resposta["messages"][-1].content)