from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

message = HumanMessage(
    content="What is LangChain?"
)

response = llm.invoke([message])

print(response)
print(type(response))
print(response.content)