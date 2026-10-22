from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


# llm = HuggingFacePipeline.from_model_id(
#     model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task = "text-generation")


llm = ChatGroq(
    model="openai/gpt-oss-120b"
)



template = PromptTemplate(
    template = "Write a detailed report on {topic}. Include an introduction, main points, and a conclusion.",
    input_variables = ["topic"]
)

template1 = PromptTemplate(
    template = "Write a 5 line summary report on the following text. /n {text}.",
    input_variables = ["text"]
)

parser = StrOutputParser()

chain = template | llm | parser | template1 | llm | parser

result = chain.invoke({'topic': 'black hole'})

print(result)