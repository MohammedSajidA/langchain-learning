from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load API key from .env
load_dotenv()

# Create the model
model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

# Create a prompt template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words for a beginner."
)

# Create an LCEL chain
chain = prompt | model

# Run the chain
response = chain.invoke({
    "topic": "LCEL in LangChain"
})

# Print the AI response
print(response.content)