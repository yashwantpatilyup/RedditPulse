

# Install necessary packages


import praw
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import os
import gradio as gr

# Download the VADER lexicon
nltk.download('vader_lexicon', quiet=True)

class RedditSentimentAgent:
    def __init__(self, client_id, client_secret, user_agent):
        # Initialize VADER sentiment analyzer
        self.sia = SentimentIntensityAnalyzer()

        # Initialize Reddit API client
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )

    def get_comments(self, subreddit_name, limit=1000):
        subreddit = self.reddit.subreddit(subreddit_name)
        comments = []
        for comment in subreddit.comments(limit=limit):
            comments.append(comment.body)
        return comments

    def analyze_sentiment(self, text):
        return self.sia.polarity_scores(text)['compound']

    def categorize_sentiment(self, score):
        if score <= -0.05:
            return 'Negative'
        elif score >= 0.05:
            return 'Positive'
        else:
            return 'Neutral'

    def analyze_subreddit(self, subreddit_name, limit=1000):
        comments = self.get_comments(subreddit_name, limit)
        sentiments = [self.analyze_sentiment(comment) for comment in comments]

        df = pd.DataFrame({'comment': comments, 'sentiment': sentiments})
        df['sentiment_category'] = df['sentiment'].apply(self.categorize_sentiment)

        return df

    def visualize_results(self, df, subreddit_name):
        # Histogram of sentiment scores
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        ax1.hist(df['sentiment'], bins=20, edgecolor='black')
        ax1.set_title(f'Sentiment Distribution in r/{subreddit_name} using VADER')
        ax1.set_xlabel('Sentiment Polarity')
        ax1.set_ylabel('Frequency')

        # Bar chart of sentiment categories
        sentiment_counts = df['sentiment_category'].value_counts()
        fig2, ax2 = plt.subplots(figsize=(8, 6))
        sentiment_counts.plot(kind='bar', ax=ax2)
        ax2.set_title(f'Sentiment Distribution in r/{subreddit_name}')
        ax2.set_xlabel('Sentiment Category')
        ax2.set_ylabel('Number of Comments')

        return fig1, fig2

    def get_statistics(self, df):
        stats = f"Average sentiment: {df['sentiment'].mean():.2f}\n"
        stats += f"Median sentiment: {df['sentiment'].median():.2f}\n"
        stats += f"Most positive comment: {df.loc[df['sentiment'].idxmax(), 'comment']}\n"
        stats += f"Most negative comment: {df.loc[df['sentiment'].idxmin(), 'comment']}\n"

        sentiment_counts = df['sentiment_category'].value_counts()
        stats += f"\nSentiment Distribution:\n{sentiment_counts}"

        return stats

    def analyze(self, subreddit_name, limit):
        try:
            df = self.analyze_subreddit(subreddit_name, limit)
            fig1, fig2 = self.visualize_results(df, subreddit_name)
            stats = self.get_statistics(df)
            return fig1, fig2, stats
        except Exception as e:
            return None, None, f"An error occurred: {str(e)}"

# Replace these with your actual Reddit API credentials
REDDIT_CLIENT_ID = "rDCXZ2gSgcW-GVwC01MlUw"
REDDIT_CLIENT_SECRET = "7_7u6nwF8Ok-il14ek2yt6rv3vg0gQ"
REDDIT_USER_AGENT = "IcyTruth4022"

agent = RedditSentimentAgent(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT)

def gradio_interface(subreddit_name, limit):
    return agent.analyze(subreddit_name, int(limit))

iface = gr.Interface(
    fn=gradio_interface,
    inputs=[
        gr.Textbox(label="Subreddit Name"),
        gr.Slider(minimum=10, maximum=1000, step=10, label="Number of Comments", value=100)
    ],
    outputs=[
        gr.Plot(label="Sentiment Distribution"),
        gr.Plot(label="Sentiment Categories"),
        gr.Textbox(label="Statistics", lines=10)
    ],
    title="Reddit Sentiment Analysis",
    description="Analyze the sentiment of comments in a subreddit using VADER."
)

iface.launch()