from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load GROQ_API_KEY from .env
load_dotenv()

# Create the model
model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

# Create a reusable prompt template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words for a beginner."
)

# Fill the {topic} variable
messages = prompt.invoke({
    "topic": "LangChain"
})

# Send the prompt to the model
response = model.invoke(messages)

# Print the answer
print(response.content)