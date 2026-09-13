from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful {role}."),
    ("human", "Explain {topic}.")
])
messages = prompt.invoke({
    "role": "teacher",
    "topic": "LCEL"
})

print(messages)