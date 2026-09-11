#StrOutputParser converts the model's output(AI Message) into a normal Python string
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

result = parser.invoke("Hello LangChain!")

print(result)
print(type(result))