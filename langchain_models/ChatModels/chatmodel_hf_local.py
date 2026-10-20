from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace


llm = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation")


model = ChatHuggingFace(llm = llm)

result = model.invoke("What is the capital of France?")
print(result.content)