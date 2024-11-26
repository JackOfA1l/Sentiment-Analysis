import streamlit as st
from sentiment import get_sentiment

# Set up the title of the app
st.title("Mood Analyzer")

# Input from the user
user_input = st.text_input("How was your day?")

# Process input and display result
if user_input:
    sentiment = get_sentiment(user_input)
    st.write(f"Your mood is: {sentiment}")
