from textblob import TextBlob

def get_sentiment(text):
    # Create a TextBlob object for the input text
    analysis = TextBlob(text)

    # Determine sentiment polarity
    if analysis.sentiment.polarity > 0:
        return "Happy"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Sad"
