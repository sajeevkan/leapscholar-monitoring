import smtplib
from email.mime.text import MIMEText
from fetch_twitter import get_tweets
from fetch_reddit import get_reddit_mentions

def build_summary():
    tweets = get_tweets()
    reddit = get_reddit_mentions()
    msg = f"LeapScholar Summary:\n\nTwitter:\n"
    for t in tweets:
        msg += f"{t['sentiment'].upper()}: {t['text']}\n"
    msg += "\nReddit:\n"
    for r in reddit:
        msg += f"{r['sentiment'].upper()}: {r['text']}\n"
    return msg

def send_email():
    content = build_summary()
    msg = MIMEText(content)
    msg["Subject"] = "Daily LeapScholar Brand Summary"
    msg["From"] = "YOUR_EMAIL"
    msg["To"] = "RECEIVER_EMAIL"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("YOUR_EMAIL", "YOUR_APP_PASSWORD")
        server.send_message(msg)
