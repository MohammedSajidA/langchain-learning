from langchain_core.runnables import RunnablePassthrough, RunnableParallel

chain = RunnableParallel(
    original=RunnablePassthrough(),
    message=lambda x: x.upper()
)

result = chain.invoke("hello langchain")

print(result)