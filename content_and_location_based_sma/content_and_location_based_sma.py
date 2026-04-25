# -*- coding: utf-8 -*-
"""sma expt9.ipynb


"""

!pip install geopandas geop/y shapely

import pandas as pd
import re

import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import geopandas as gpd
from geopy.geocoders import Nominatim
from shapely.geometry import Point
import time

data = {
'Text': [
"Great meeting with @user1 today!",
"Thanks @user2 and @user1 for the support!",
"@user3 is doing amazing work!",
"Follow @user2 and @user4 for updates",
"@user1 @user2 @user3 are top contributors!"
]
}

df = pd.DataFrame(data)
print(df)

def extract_mentions(text):
  return re.findall(r'@\w+', text)
df['Mentions'] = df['Text'].apply(extract_mentions)
print(df[['Text', 'Mentions']])

all_mentions = [mention for sublist in df['Mentions'] for mention in sublist]
mention_count = Counter(all_mentions)
mention_df = pd.DataFrame(mention_count.items(), columns=['User', 'Count'])
mention_df = mention_df.sort_values(by='Count', ascending=False)
print(mention_df)

plt.figure(figsize=(8,5))
sns.barplot(x='User', y='Count', data=mention_df)
plt.title("Top Mentioned Users")
plt.xticks(rotation=45)
plt.show()

location_data = {
'Review': [
"Good product", "Excellent service", "Average experience",
"Not satisfied", "Loved it!"
],
'Location': [
"Mumbai", "Delhi", "New York", "London", "Tokyo"
]
}

loc_df = pd.DataFrame(location_data)
print(loc_df)

geolocator = Nominatim(user_agent="geo_app")
def get_coordinates(location):
  try:
    loc = geolocator.geocode(location)
    time.sleep(1) # avoid API blocking
    if loc:
      return loc.latitude, loc.longitude
    else:
      return None, None
  except:
    return None, None
loc_df[['Latitude', 'Longitude']] = loc_df['Location'].apply(
lambda x: pd.Series(get_coordinates(x))
)
print(loc_df)

geometry = [Point(xy) for xy in zip(loc_df['Longitude'], loc_df['Latitude'])]
geo_df = gpd.GeoDataFrame(loc_df, geometry=geometry)
geo_df = geo_df.dropna()

import geopandas as gpd
# Load world map from online source
world = gpd.read_file("https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_countries.zip")

plt.figure(figsize=(10,6))
ax = world.plot()
geo_df.plot(ax=ax, markersize=50, color='red', edgecolor='black', alpha=1)
plt.title("Geographic Distribution of Reviews")
plt.show()



"""# Exercise 1"""

import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

data = {
    'Text': [
        "Excited about deep learning! #DeepLearning #AI",
        "Analyzing datasets all day #DataAnalytics #BigData",
        "Building cool projects with Python #Python #Dev",
        "AI is transforming the future #AI #Innovation",
        "Coding and debugging fun #Programming #Coding",
        "Understanding neural networks #DeepLearning #ML",
        "Visualizing data insights #DataViz #Analytics",
        "Automation using Python scripts #Python #Automation",
        "Tech trends to watch #Technology #AI",
        "Sharpening coding skills daily #Coding #Developer"
    ]
}
df = pd.DataFrame(data)
print(df)

def extract_hashtags(text):
  return re.findall(r'#\w+', text)
df['Hashtags'] = df['Text'].apply(extract_hashtags)
print(df[['Text', 'Hashtags']])

all_tags = [tag for sublist in df['Hashtags'] for tag in sublist]
tag_count = Counter(all_tags)
tag_df = pd.DataFrame(tag_count.items(), columns=['Hashtag', 'Count'])
tag_df = tag_df.sort_values(by='Count', ascending=False)
print(tag_df)

plt.figure(figsize=(8,5))
sns.barplot(x='Hashtag', y='Count', data=tag_df)
plt.title("Top Trending Hashtags")
plt.xticks(rotation=45)
plt.show()



"""# Exercise 2"""

!pip install textblob

import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Review': [
        "Amazing service, highly recommend",
        "Terrible quality, not worth it",
        "It was okay, nothing special",
        "Really impressed with the product",
        "Very poor experience, will not return"
    ],
    'Location': [
        "Bangalore", "Pune", "Bangalore", "Chennai", "Pune"
    ]
}
df = pd.DataFrame(data)
print(df)

def get_sentiment(text):
  polarity = TextBlob(text).sentiment.polarity
  if polarity > 0:
      return "Positive"
  elif polarity < 0:
    return "Negative"
  else:
    return "Neutral"
df['Sentiment'] = df['Review'].apply(get_sentiment)
print(df)

sentiment_count = df.groupby(['Location', 'Sentiment']).size().unstack().fillna(0)
print(sentiment_count)

sentiment_count.plot(kind='bar', figsize=(8,5))
plt.title("Sentiment Distribution by Location")
plt.xlabel("Location")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.show()

# Geocode locations for the sentiment analysis data
sentiment_df = df.copy()
sentiment_df[['Latitude', 'Longitude']] = sentiment_df['Location'].apply(
    lambda x: pd.Series(get_coordinates(x))
)

# Create a GeoDataFrame for the sentiment data
geometry_sentiment = [Point(xy) for xy in zip(sentiment_df['Longitude'], sentiment_df['Latitude'])]
geo_sentiment_df = gpd.GeoDataFrame(sentiment_df, geometry=geometry_sentiment)
geo_sentiment_df = geo_sentiment_df.dropna() # Drop rows where geocoding failed

# Plot the world map and overlay sentiment locations
plt.figure(figsize=(12, 8))
ax = world.plot() # Removed explicit color='lightgray' to use default blueish map

# Plot sentiments with different colors
geo_sentiment_df[geo_sentiment_df['Sentiment'] == 'Positive'].plot(
    ax=ax, markersize=20, color='green', edgecolor='black', alpha=1, label='Positive Sentiment'
)
geo_sentiment_df[geo_sentiment_df['Sentiment'] == 'Negative'].plot(
    ax=ax, markersize=20, color='red', edgecolor='black', alpha=1, label='Negative Sentiment'
)
geo_sentiment_df[geo_sentiment_df['Sentiment'] == 'Neutral'].plot(
    ax=ax, markersize=20, color='blue', edgecolor='black', alpha=1, label='Neutral Sentiment'
)

plt.title("Geographic Distribution of Sentiment Reviews")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend()
plt.show()

world_asia = world[world['CONTINENT'] == 'Asia']

plt.figure(figsize=(12, 8))
ax = world_asia.plot()

# Plot sentiments with different colors
geo_sentiment_df[geo_sentiment_df['Sentiment'] == 'Positive'].plot(
    ax=ax, markersize=20, color='green', edgecolor='black', alpha=1, label='Positive Sentiment'
)
geo_sentiment_df[geo_sentiment_df['Sentiment'] == 'Negative'].plot(
    ax=ax, markersize=20, color='red', edgecolor='black', alpha=1, label='Negative Sentiment'
)
geo_sentiment_df[geo_sentiment_df['Sentiment'] == 'Neutral'].plot(
    ax=ax, markersize=20, color='blue', edgecolor='black', alpha=1, label='Neutral Sentiment'
)

plt.title("Geographic Distribution of Sentiment Reviews")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend()
plt.show()

