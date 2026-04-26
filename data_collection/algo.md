# Algorithm: YouTube Comment Collection & Sentiment Analysis

## Experiment 2 — Data Collection from YouTube

---

### Algorithm

```
1. START

2. Import required libraries:
      requests, textblob, pandas

3. Define YouTube video_id and api_key

4. FETCH VIDEO INFORMATION:
      a. Construct video info URL using video_id and api_key
      b. Send GET request to YouTube Data API v3
      c. Parse JSON response to get video metadata (title, channel, etc.)
      d. Display video information

5. FETCH COMMENTS:
      a. Construct commentThreads API URL using video_id and api_key
      b. Send GET request to YouTube Data API v3
      c. Parse JSON response

6. EXTRACT COMMENTS:
      a. Iterate through response["items"]
      b. For each item, extract:
            item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
      c. Store all comments in a list

7. SENTIMENT ANALYSIS ON EACH COMMENT:
      FOR each comment in comments list:
         a. Create TextBlob object from comment text
         b. Compute polarity score using TextBlob.sentiment.polarity
         c. Classify sentiment:
            - polarity > 0      → "Positive"
            - polarity == 0     → "Neutral"
            - polarity < 0      → "Negative"
         d. Store comment and its sentiment label

8. CREATE DATAFRAME:
      a. Create pandas DataFrame with columns:
         - "Comments"  : original comment text
         - "Sentiment" : classified sentiment label
      b. Display the DataFrame

9. EXPORT RESULTS:
      a. Save DataFrame to "YouTube_Comments_Sentiment.csv"
      b. Set index=False to exclude row indices

10. END
```

---

### Key Components

| Component            | Description                                          |
|----------------------|------------------------------------------------------|
| **API Used**         | YouTube Data API v3 (`commentThreads` endpoint)      |
| **Sentiment Engine** | TextBlob (polarity-based classification)             |
| **Output**           | CSV file with comments and their sentiment labels    |

### Polarity Thresholds

| Polarity Value   | Sentiment  |
|------------------|------------|
| `> 0`            | Positive   |
| `== 0`           | Neutral    |
| `< 0`            | Negative   |
