from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

messages = [
    SystemMessage(
        content="You are a teacher. Explain things simply."
    ),
    HumanMessage(
        content="What is LCEL?"
    )
]

response = llm.invoke(messages)

print("RESPONSE TYPE:")
print(type(response))

print("\nAI MESSAGE:")
print(response)

print("\nCONTENT:")
print(response.content)

print("\nCONTENT TYPE:")
print(type(response.content))