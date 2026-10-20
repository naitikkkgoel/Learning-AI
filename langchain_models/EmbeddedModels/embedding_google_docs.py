from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model = "gemini-embedding-2",
    dimensions = 32)

documents = [
    "Delhi is the capital of India.",
    "Paris is the capital of France.",
    "Berlin is the capital of Germany.",
    "Tokyo is the capital of Japan.",
    "Canberra is the capital of Australia."]

embedding_vectors = embeddings.embed_documents(documents)

print(str(embedding_vectors))