from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Create the model
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

# Create the chain
chain = (
    RunnablePassthrough()
    | llm
    | StrOutputParser()
)

# Run the chain
result = chain.invoke(
    "Explain RunnablePassthrough in one simple sentence."
)

print(result)