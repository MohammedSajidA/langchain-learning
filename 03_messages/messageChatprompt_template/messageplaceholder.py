from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)
from langchain_core.messages import (
    HumanMessage,
    AIMessage
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),

    MessagesPlaceholder("history"),

    ("human", "{question}")
])

history = [
    HumanMessage(content="What is Python?"),
    AIMessage(content="Python is a programming language.")
]

messages = prompt.invoke({
    "history": history,
    "question": "What is a variable?"
})

print(messages)
print("\nActual messages:")
print(messages.messages)