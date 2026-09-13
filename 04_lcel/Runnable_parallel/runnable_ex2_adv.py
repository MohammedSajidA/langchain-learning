from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser


# Load GROQ_API_KEY from .env
load_dotenv()


# Create the ChatGroq model
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)


# Create three different prompts
explanation_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} to a beginner in 2 simple sentences."
)

advantages_prompt = ChatPromptTemplate.from_template(
    "Give 3 important advantages of {topic}."
)

example_prompt = ChatPromptTemplate.from_template(
    "Give one simple real-world example of {topic}."
)


# Create three separate chains
explanation_chain = explanation_prompt | llm | StrOutputParser()

advantages_chain = advantages_prompt | llm | StrOutputParser()

example_chain = example_prompt | llm | StrOutputParser()


# Run all three chains in parallel
parallel_chain = RunnableParallel(
    explanation=explanation_chain,
    advantages=advantages_chain,
    example=example_chain
)


# Run the parallel chain
result = parallel_chain.invoke({
    "topic": "Artificial Intelligence"
})


# Print the results
print("\n===== EXPLANATION =====")
print(result["explanation"])

print("\n===== ADVANTAGES =====")
print(result["advantages"])

print("\n===== REAL-WORLD EXAMPLE =====")
print(result["example"])

print(result)