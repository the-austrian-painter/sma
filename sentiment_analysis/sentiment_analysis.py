# -*- coding: utf-8 -*-
"""sma expt 4.ipynb

"""

!pip install google-api-python-client pandas textblob wordcloud matplotlib nltk

import pandas as pd
import re
import nltk
from textblob import TextBlob
from googleapiclient.discovery import build
from wordcloud import WordCloud
import matplotlib.pyplot as plt
nltk.download('punkt')

api_key = "AIzaSyBWaideHJkPuTDeSKfeZ5bzx-NjnNh3KfU"
youtube = build('youtube', 'v3', developerKey=api_key)

video_id = "CodKaNudr9E"
comments = []
request = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    maxResults=100
)
response = request.execute()
for item in response['items']:
    comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
    comments.append(comment)
df = pd.DataFrame(comments, columns=['Comment'])
df.head()

df.to_csv("youtube_comments.csv", index=False)
df.to_json("youtube_comments.json")

import pandas as pd
# Load JSON
df = pd.read_json("youtube_comments.json")
# Convert nested structure to proper column
df = df['Comment'].reset_index()
df.columns = ['ID', 'Comment']
df.head()

import re
def clean_text(text):
    text = re.sub(r'http\S+', '', text)     # remove links
    text = re.sub(r'<.*?>', '', text)       # remove html tags
    text = re.sub(r'[^A-Za-z ]', '', text)  # remove symbols
    text = text.lower()
    return text
df['Cleaned'] = df['Comment'].astype(str).apply(clean_text)
df.head()

from textblob import TextBlob
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"
df['Sentiment'] = df['Cleaned'].apply(get_sentiment)
df.head()

from wordcloud import WordCloud
import matplotlib.pyplot as plt
def generate_wordcloud(sentiment):
    text = " ".join(df[df['Sentiment'] == sentiment]['Cleaned'])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(8,4))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.title(sentiment + " Word Cloud")
    plt.show()
generate_wordcloud("Positive")
generate_wordcloud("Negative")
generate_wordcloud("Neutral")

df['Sentiment'].value_counts().plot(kind='bar')
plt.title("Sentiment Distribution")
plt.show()

!pip install google-play-scraper

from google_play_scraper import reviews
import pandas as pd
result, _ = reviews(
    'in.startv.hotstar',
    lang='en',
    country='in',
    count=200
)
df_hotstar = pd.DataFrame(result)
df_hotstar = df_hotstar[['content']]   # keep only review text
df_hotstar.columns = ['Comment']
df_hotstar.head()

df_hotstar.to_csv("df_hotstar.csv", index=False)

from google_play_scraper import reviews
import pandas as pd
result, _ = reviews(
    'com.netflix.mediaclient',
    lang='en',
    country='in',
    count=200
)
df_netflix = pd.DataFrame(result)
df_netflix = df_netflix[['content']]
df_netflix.columns = ['Comment']
df_netflix.head()

df_netflix.to_csv("df_netflix.csv", index=False)

import re
def clean_text(text):
    text = re.sub(r'http\S+', '', str(text))
    text = re.sub(r'[^A-Za-z ]', '', text)
    text = text.lower()
    return text
df_netflix['Cleaned'] = df_netflix['Comment'].apply(clean_text)
df_netflix['Cleaned'] = df_netflix['Comment'].apply(clean_text)
from textblob import TextBlob
def get_polarity(text):
    return TextBlob(text).sentiment.polarity
df_netflix['Polarity'] = df_netflix['Cleaned'].apply(get_polarity)
df_netflix['Polarity'] = df_netflix['Cleaned'].apply(get_polarity)
def get_sentiment(score):
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"
df_netflix['Sentiment'] = df_netflix['Polarity'].apply(get_sentiment)
df_netflix['Sentiment'] = df_netflix['Polarity'].apply(get_sentiment)
df_netflix[['Comment','Cleaned','Polarity','Sentiment']].head(10)

df_netflix[['Comment','Cleaned','Polarity','Sentiment']].head(10)

import matplotlib.pyplot as plt
import pandas as pd

# Assuming clean_text, get_polarity, get_sentiment functions are already defined
# Process df_spotify to add 'Cleaned', 'Polarity', 'Sentiment' columns
df_hotstar['Cleaned'] = df_hotstar['Comment'].apply(clean_text)
df_hotstar['Polarity'] = df_hotstar['Cleaned'].apply(get_polarity)
df_hotstar['Sentiment'] = df_hotstar['Polarity'].apply(get_sentiment)

comparison_df = pd.DataFrame({
    'JioHotstar': df_hotstar['Sentiment'].value_counts(),
    'Netflix': df_netflix['Sentiment'].value_counts()}).fillna(0)
comparison_df.plot(kind='bar')
plt.title("JioHotstar vs Netflix Sentiment Comparison")
plt.xlabel("Sentiment Type")
plt.ylabel("Number of Reviews")
plt.show()

