import streamlit as st
import textwrap
import google.generativeai as genai
from PIL import Image
import markdownify

# Set up authentication with the API using your API key
genai.configure(api_key="")

def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize our Streamlit app
st.set_page_config(page_title="🤖Bard-AI[image]")

st.header("🤖Bard-AI[image]")
input_text = st.text_input("Input Prompt:", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the image")

# If submit button is clicked
if submit:
    response = get_gemini_response(input_text, image)
    markdown_response = markdownify.markdownify(response)
    st.subheader("")
    st.markdown(markdown_response)

