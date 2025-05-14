import streamlit as st
from transformers import pipeline

sentiment = pipeline('sentiment-analysis')
st.title("Sentiment Analyser")
user_input = st.text_input("Enter the sentence")
if st.button("Get Sentiment"):
    if user_input:
        result = sentiment(user_input)
        st.write(f"sentiment is '{result[0]['label']}'")