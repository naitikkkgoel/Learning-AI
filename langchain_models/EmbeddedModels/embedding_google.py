from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model = "gemini-embedding-2",
    dimensions = 32)

embedding_vector = embeddings.embed_query("Delhi is the capital of India.")

print(str(embedding_vector))