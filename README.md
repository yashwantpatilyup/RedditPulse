# RedditPulse
A reddit post and comment sentiment analysis using reddit api with gradio UI


# Real-Time Reddit Sentiment Analysis

## Overview
This project is a **Real-Time Reddit Sentiment Analysis Tool** that allows users to fetch the latest posts from any subreddit and analyze their sentiment dynamically. The project uses the **VADER Sentiment Analyzer** to classify the sentiment of Reddit posts into Positive, Negative, or Neutral categories and displays results in real-time via a user-friendly **Gradio interface**.

## Features
1. **Real-Time Sentiment Analysis**:
   - Fetches the latest posts from a specified subreddit using the Reddit API.
   - Analyzes the sentiment of the posts' titles using the VADER sentiment analyzer.
2. **Interactive UI**:
   - Built with Gradio for an intuitive and responsive user experience.
   - Users can input a subreddit name and choose the number of posts to analyze.
3. **Dynamic Sentiment Visualization** (Optional):
   - Real-time sentiment scores are visualized using Plotly.
4. **Average Sentiment Score**:
   - Calculates the average sentiment score of the fetched posts.
5. **Top Posts Sentiment**:
   - Displays the sentiment of individual posts (title, sentiment category, and sentiment score).

## Technologies Used
- **Python**: Core programming language for the project.
- **PRAW (Python Reddit API Wrapper)**: To fetch real-time data from Reddit.
- **VADER Sentiment Analyzer**: For natural language processing and sentiment classification.
- **Gradio**: For building the interactive user interface.
- **Plotly** (Optional): For live data visualization.

## Requirements
- Python 3.8+
- Dependencies:
  ```bash
  pip install praw gradio vaderSentiment plotly
  ```

## How It Works
1. **Fetching Reddit Data**:
   - Uses the Reddit API (via PRAW) to fetch the latest posts from a user-specified subreddit.
   - Posts are fetched dynamically based on user input.
2. **Sentiment Analysis**:
   - The **VADER Sentiment Analyzer** calculates sentiment scores for each post title.
   - Sentiments are categorized as:
     - **Positive**: Compound score > 0
     - **Negative**: Compound score < 0
     - **Neutral**: Compound score = 0
3. **Display Results**:
   - The results include:
     - **Average sentiment score** of all posts.
     - Sentiment details (title, score, and category) for individual posts.
4. **Interactive Interface**:
   - A Gradio UI allows users to enter the subreddit name and number of posts to analyze.
   - Real-time updates ensure the latest data is fetched and analyzed.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yashwantpatilyup/RedditPulse.git
   cd RedditPulse
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open the Gradio interface in your browser to interact with the app.

## Example
1. Enter a subreddit name (e.g., `python`).
2. Choose the number of posts to fetch (e.g., 10).
3. View the following outputs:
   - **Average Sentiment Score**: An overall sentiment score for the subreddit.
   - **Top Posts Sentiment**: The sentiment details for the top 10 posts.
   - (Optional) **Visualization**: A live bar chart showing sentiment scores for all posts.

## Deployment
- The application can be deployed on platforms like:
  - **Hugging Face Spaces**: Free hosting for Gradio apps.
  - **Streamlit Sharing** or **Google Cloud Run**.
  - **AWS, Azure, or Heroku** for scalable deployment.

## Future Enhancements
1. **Comment Sentiment Analysis**:
   - Extend the functionality to analyze sentiment from comments.
2. **Historical Sentiment Trends**:
   - Compare sentiment over time by fetching older posts.
3. **Alert System**:
   - Notify users when sentiment exceeds a threshold.
4. **Advanced NLP Models**:
   - Integrate models like BERT or GPT for more nuanced sentiment analysis.
5. **Live Sentiment Dashboard**:
   - Add real-time data visualization with live graphs.

## Credits
- **PRAW**: For seamless Reddit API integration.
- **VADER Sentiment Analyzer**: For accurate sentiment classification.
- **Gradio**: For the interactive and user-friendly interface.
- **Plotly**: For optional visualization features.

---

Feel free to contribute to this project by submitting issues or pull requests!

