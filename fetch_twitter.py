import tweepy
from textblob import TextBlob

bearer_token = "YOUR_TWITTER_BEARER_TOKEN"

client = tweepy.Client(bearer_token=bearer_token)

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "positive"
    elif polarity == 0:
        return "neutral"
    else:
        return "negative"

def get_tweets(query="LeapScholar", max_results=20):
    tweets = client.search_recent_tweets(query=query, max_results=max_results)
    results = []
    if tweets.data:
        for tweet in tweets.data:
            sentiment = analyze_sentiment(tweet.text)
            results.append({"text": tweet.text, "sentiment": sentiment})
    return results
