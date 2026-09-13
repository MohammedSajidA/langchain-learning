from langchain_core.prompts import HumanMessagePromptTemplate

template = HumanMessagePromptTemplate.from_template(
    "Explain {topic} to me."
)

message = template.invoke({
    "topic": "Python"
})

print(message)