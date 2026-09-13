from langchain_core.runnables import RunnableParallel, RunnablePassthrough


# Create a parallel runnable
chain = RunnableParallel(
    original=RunnablePassthrough(),
    uppercase=lambda x: x.upper(),
    length=lambda x: len(x)
)


# Run the chain
result = chain.invoke("hello langchain")


# Print the result
print(result)
