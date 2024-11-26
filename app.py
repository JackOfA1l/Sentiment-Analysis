import streamlit as st
from sentiment import get_sentiment

# Set up the title of the app
st.set_page_config(page_title="Mood Analyzer", page_icon="🧠", layout="wide")
st.title("🌞 Mood Analyzer 🌞")

# Add some space and a subtitle
st.subheader("Tell us how your day was, and we'll help you analyze your mood!")

# Input from the user
user_input = st.text_input("How was your day? 🗣️", placeholder="Share your thoughts...")

# Process input and display result
if user_input:
    sentiment = get_sentiment(user_input)
    if sentiment == 'Happy':
        st.markdown(f"<h3 style='color: green;'>😊 Your mood is: {sentiment}</h3>", unsafe_allow_html=True)
    elif sentiment == 'Neutral':
        st.markdown(f"<h3 style='color: grey;'>😐 Your mood is: {sentiment}</h3>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h3 style='color: red;'>😞 Your mood is: {sentiment}</h3>", unsafe_allow_html=True)

    # Add some more interaction
    st.markdown("---")
    st.write("Need advice to feel better? Here's a tip:")
    st.write("💡 **Take a deep breath and relax! Everything will be okay.**")

