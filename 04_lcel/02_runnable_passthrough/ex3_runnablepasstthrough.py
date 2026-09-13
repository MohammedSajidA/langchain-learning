from langchain_core.runnables import RunnablePassthrough


# Step 1: Pass the input without changing it
passthrough = RunnablePassthrough()


# Step 2: Transform the input
uppercase = lambda x: x.upper()


# Step 3: Connect them using LCEL
chain = passthrough | uppercase


# Run the chain
result = chain.invoke("hello langchain")

print(result)