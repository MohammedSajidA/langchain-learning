from langchain_core.messages import HumanMessage

message = HumanMessage(
    content="What is LangChain?"
)

print(message)
print(type(message))
print(message.content)