from langchain_core.runnables import RunnablePassthrough

# Create RunnablePassthrough
passthrough = RunnablePassthrough()

# Send input through it
result = passthrough.invoke("Hello LangChain!")

print(result)