import streamlit as st
import textwrap
import google.generativeai as genai

#Set up authentication with the API using your API key
genai.configure(api_key="")


# Initialize the model you want to use
model = genai.GenerativeModel('gemini-pro')

# Function to convert text to Markdown format
def to_markdown(text):
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

st.title('🤖Bard-AI[Chat]')
prompt = st.text_input('Enter your prompt here!')

if prompt:
    response = model.generate_content(prompt)
    # Ensure the response is resolved before accessing the text
    response.resolve()
    markdown_content = to_markdown(response.text)
    st.markdown(markdown_content, unsafe_allow_html=True)
