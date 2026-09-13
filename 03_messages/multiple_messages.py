from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

messages = [
    SystemMessage(
        content="You are a helpful programming teacher."
    ),

    HumanMessage(
        content="What is Python?"
    ),

    AIMessage(
        content="Python is a programming language."
    ),

    HumanMessage(
        content="What is a variable?"
    )
]

response = llm.invoke(messages)

print(response.content)