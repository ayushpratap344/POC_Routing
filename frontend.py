import streamlit as st
from backend import get_groq_response , MODEL_NAME 

st.image("logo_2.png", width=300)

st.title("Chatbot Query~Pilots POC")

with open("design.css") as f:
    css = f.read()

st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

user_input = st.text_input("Ask your question:")

if st.button("Submit"):
    if user_input:
        response,time_taken = get_groq_response(user_input)
        st.write("Response:", response)
        st.markdown(f"**Model being used:** {MODEL_NAME}")
        st.markdown(f"**Time taken:** {time_taken:.2f} seconds")
    else:
        st.warning("Please enter a question.")
