from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert {subject} teacher."),
    ("human", "Explain {topic} to me in simple words.")
])

chain = prompt | llm

response = chain.invoke({
    "subject": "Python",
    "topic": "variables"
})

print(response)
print(type(response))
print(response.content)