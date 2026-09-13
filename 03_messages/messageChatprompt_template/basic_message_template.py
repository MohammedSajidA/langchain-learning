from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

system_template = SystemMessagePromptTemplate.from_template(
    "You are an expert {subject} teacher."
)

human_template = HumanMessagePromptTemplate.from_template(
    "Explain {topic} to me in simple words."
)

prompt = ChatPromptTemplate.from_messages([
    system_template,
    human_template
])

messages = prompt.invoke({
    "subject": "Python",
    "topic": "variables"
})

print(messages)