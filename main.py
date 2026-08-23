from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load the API key from .env
load_dotenv()

# Create the AI model
model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

# Send a message to the AI
response = model.invoke(
    "What is Artificial Intelligence? Explain in 3 simple points."
)

# Print only the AI's text response
print(response.content)