from langchain_groq import ChatGroq
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()
model = ChatGroq(
    model = "openai/gpt-oss-120b")

st.header("Research Assistant")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = PromptTemplate(
    template="""
    Please summarize the reasearch paper titled "{paper_title}" with the following specifications:
    Explanation Style: {explanation_style}
    Explanation Length: {explanation_length}
    1. Mathematical Details
        - Include relevant mathematical equations and derivations where applicable.
        - Explain mathematical concepts in a clear and concise manner, providing step-by-step explanations.
    2. Analogies and Examples
        - Use analogies and real-world examples to illustrate complex concepts.
        - Provide practical applications of the research findings.
    If certain details are not available in the paper, please indicate that they are not present by returning "Insufficient information provided in the paper."    
    """,
    input_variables=["paper_title", "explanation_style", "explanation_length"]
)

prompt = template.invoke({
    "paper_title": paper_input,
    "explanation_style": style_input,
    "explanation_length": length_input
})

if st.button('summarize'):
    result = model.invoke(prompt)
    st.write(result.content)