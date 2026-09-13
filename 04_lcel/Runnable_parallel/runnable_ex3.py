from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


# Load GROQ_API_KEY from .env
load_dotenv()


# Create the model
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)


# -------------------------------
# PARALLEL PART
# -------------------------------

parallel_chain = RunnableParallel(
    original=RunnablePassthrough(),

    explanation=(
        ChatPromptTemplate.from_template(
            "Explain {topic} to a beginner in 2 simple sentences."
        )
        | llm
        | StrOutputParser()
    ),

    advantages=(
        ChatPromptTemplate.from_template(
            "Give 3 important advantages of {topic}."
        )
        | llm
        | StrOutputParser()
    )
)


# -------------------------------
# FINAL PROMPT
# -------------------------------

final_prompt = ChatPromptTemplate.from_template(
    """
You are given information about a topic.

Original topic:
{original}

Explanation:
{explanation}

Advantages:
{advantages}

Using the information above, give a short and clear final answer about the topic.
"""
)


# -------------------------------
# COMPLETE CHAIN
# -------------------------------

final_chain = parallel_chain | final_prompt | llm | StrOutputParser()


# -------------------------------
# RUN
# -------------------------------

result = final_chain.invoke({
    "topic": "Artificial Intelligence"
})


print("\n===== FINAL ANSWER =====")
print(result)