from langchain_core.runnables import RunnableBranch


# Branch when the input contains "math"
math_branch = lambda x: "This is a math question."


# Default branch
general_branch = lambda x: "This is a general question."


# Create the branch
branch = RunnableBranch(
    (lambda x: "math" in x.lower(), math_branch),
    general_branch
)


# Test 1
result1 = branch.invoke("Can you help me with math?")
print(result1)


# Test 2
result2 = branch.invoke("What is LangChain?")
print(result2)