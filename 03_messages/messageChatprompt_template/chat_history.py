from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# Load API key
load_dotenv()

# Create model
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

# Create prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful programming teacher."),

    # Insert previous conversation here
    MessagesPlaceholder("history"),

    # Current user question
    ("human", "{question}")
])

# Previous conversation
history = [
    HumanMessage(content="What is Python?"),
    AIMessage(content="Python is a programming language."),
    HumanMessage(content="What is a variable?"),
    AIMessage(content="A variable is a name used to store a value.")
]

# Create LCEL chain
chain = prompt | llm

# Ask a new question
response = chain.invoke({
    "history": history,
    "question": "What did we discuss earlier?"
})
print(response.content)