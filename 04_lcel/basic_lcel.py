from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load GROQ_API_KEY from .env
load_dotenv()

# Create the ChatGroq model
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

# Create the prompt template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} to a beginner in exactly 3 simple points."
)

# Create the LCEL chain
chain = prompt | llm | StrOutputParser()

# Run the chain
result = chain.invoke({
    "topic": "LCEL in LangChain"
})

# Print the final text
print(result)
