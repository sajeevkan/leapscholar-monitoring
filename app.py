import streamlit as st
from fetch_twitter import get_tweets
from fetch_reddit import get_reddit_mentions
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(page_title="LeapScholar Brand Monitor")

st.title("📊 LeapScholar Brand Monitor")

twitter_data = get_tweets()
reddit_data = get_reddit_mentions()

def count_sentiments(data):
    pos = sum(1 for x in data if x["sentiment"] == "positive")
    neu = sum(1 for x in data if x["sentiment"] == "neutral")
    neg = sum(1 for x in data if x["sentiment"] == "negative")
    return pos, neu, neg

st.subheader("Twitter Mentions")
tp, tn, tneg = count_sentiments(twitter_data)
st.write(f"Positive: {tp} | Neutral: {tn} | Negative: {tneg}")
for t in twitter_data:
    st.markdown(f"- *{t['sentiment'].upper()}*: {t['text']}")

st.subheader("Reddit Mentions")
rp, rn, rneg = count_sentiments(reddit_data)
st.write(f"Positive: {rp} | Neutral: {rn} | Negative: {rneg}")
for r in reddit_data:
    st.markdown(f"- *{r['sentiment'].upper()}*: {r['text']}")

# Word cloud
words = " ".join(t["text"] for t in twitter_data + reddit_data)
wc = WordCloud(width=800, height=400).generate(words)
st.subheader("🧠 Trending Keywords")
st.image(wc.to_array())
