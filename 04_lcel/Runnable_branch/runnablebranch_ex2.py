from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableBranch
from langchain_core.output_parsers import StrOutputParser


# Load GROQ_API_KEY from .env
load_dotenv()


# Create the ChatGroq model
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)


# -----------------------------
# MATH CHAIN
# -----------------------------

math_prompt = ChatPromptTemplate.from_template(
    """
You are a math tutor.

Solve the following math question step-by-step
and explain it to a beginner:

{question}
"""
)

math_chain = math_prompt | llm | StrOutputParser()


# -----------------------------
# GENERAL CHAIN
# -----------------------------

general_prompt = ChatPromptTemplate.from_template(
    """
You are a helpful general assistant.

Answer the following question clearly
and simply:

{question}
"""
)

general_chain = general_prompt | llm | StrOutputParser()


# -----------------------------
# RUNNABLE BRANCH
# -----------------------------

branch = RunnableBranch(
    (
        lambda x: any(
            operator in x["question"].lower()
            for operator in ["+", "-", "*", "/", "calculate"]
        ),
        math_chain
    ),
    general_chain
)


# -----------------------------
# TEST 1
# -----------------------------

result1 = branch.invoke({
    "question": "What is 25 * 4?"
})

print("\n===== QUESTION 1 =====")
print(result1)


# -----------------------------
# TEST 2
# -----------------------------

result2 = branch.invoke({
    "question": "What is LangChain?"
})

print("\n===== QUESTION 2 =====")
print(result2) 