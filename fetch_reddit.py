import praw
from textblob import TextBlob

reddit = praw.Reddit(
    client_id="YOUR_REDDIT_CLIENT_ID",
    client_secret="YOUR_REDDIT_SECRET",
    user_agent="LeapScholarMonitor"
)

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "positive"
    elif polarity == 0:
        return "neutral"
    else:
        return "negative"

def get_reddit_mentions(keyword="LeapScholar", limit=20):
    results = []
    for submission in reddit.subreddit("all").search(keyword, limit=limit):
        sentiment = analyze_sentiment(submission.title + " " + submission.selftext)
        results.append({"text": submission.title, "sentiment": sentiment})
    return results
