# Algorithm: Sentiment Analysis on YouTube & Google Play Reviews

## Experiment 4 — Sentiment Analysis

---

### Part A: YouTube Comments Sentiment Analysis

```
1. START

2. Import required libraries:
      pandas, re, nltk, textblob, googleapiclient,
      wordcloud, matplotlib

3. INITIALIZE YouTube API CLIENT:
      a. Set api_key and video_id
      b. Build YouTube service object using build('youtube', 'v3', developerKey=api_key)

4. FETCH YOUTUBE COMMENTS:
      a. Create commentThreads request with:
         - part = "snippet"
         - videoId = video_id
         - maxResults = 100
      b. Execute request and parse response
      c. Extract top-level comment text from each item
      d. Store in list and create DataFrame with column 'Comment'

5. SAVE RAW DATA:
      a. Export to "youtube_comments.csv"
      b. Export to "youtube_comments.json"

6. LOAD AND RESHAPE JSON:
      a. Read JSON file into DataFrame
      b. Flatten nested 'Comment' column
      c. Rename columns to ['ID', 'Comment']

7. CLEAN TEXT:
      FOR each comment:
         a. Remove URLs         → re.sub(r'http\S+', '', text)
         b. Remove HTML tags    → re.sub(r'<.*?>', '', text)
         c. Remove symbols      → re.sub(r'[^A-Za-z ]', '', text)
         d. Convert to lowercase
      Store in 'Cleaned' column

8. CLASSIFY SENTIMENT:
      FOR each cleaned text:
         a. Compute polarity = TextBlob(text).sentiment.polarity
         b. Classify:
            - polarity > 0   → "Positive"
            - polarity < 0   → "Negative"
            - polarity == 0  → "Neutral"
      Store in 'Sentiment' column

9. GENERATE WORD CLOUDS:
      FOR each sentiment in ["Positive", "Negative", "Neutral"]:
         a. Filter DataFrame where Sentiment == sentiment
         b. Join all cleaned text
         c. Generate WordCloud (800x400, white background)
         d. Display with matplotlib

10. PLOT SENTIMENT DISTRIBUTION:
      a. Count sentiment value_counts()
      b. Display as bar chart
```

---

### Part B: Google Play Reviews — JioHotstar vs Netflix

```
11. SCRAPE JIOHOTSTAR REVIEWS:
      a. Use google_play_scraper.reviews() with:
         - app_id = 'in.startv.hotstar'
         - lang = 'en', country = 'in', count = 200
      b. Extract 'content' column → DataFrame with 'Comment'
      c. Save to "df_hotstar.csv"

12. SCRAPE NETFLIX REVIEWS:
      a. Use google_play_scraper.reviews() with:
         - app_id = 'com.netflix.mediaclient'
         - lang = 'en', country = 'in', count = 200
      b. Extract 'content' column → DataFrame with 'Comment'
      c. Save to "df_netflix.csv"

13. CLEAN NETFLIX REVIEWS:
      FOR each comment in df_netflix:
         a. Remove URLs, non-alphabetic characters
         b. Convert to lowercase
      Store in 'Cleaned' column

14. COMPUTE POLARITY (Netflix):
      FOR each cleaned text:
         polarity = TextBlob(text).sentiment.polarity
      Store in 'Polarity' column

15. CLASSIFY SENTIMENT (Netflix):
      FOR each polarity score:
         - score > 0   → "Positive"
         - score < 0   → "Negative"
         - score == 0  → "Neutral"
      Store in 'Sentiment' column

16. CLEAN & CLASSIFY JIOHOTSTAR REVIEWS:
      a. Apply same clean_text() function
      b. Apply same get_polarity() function
      c. Apply same get_sentiment() function

17. COMPARE SENTIMENTS:
      a. Create comparison DataFrame with:
         - 'JioHotstar' : sentiment value counts
         - 'Netflix'    : sentiment value counts
      b. Fill missing values with 0
      c. Plot grouped bar chart for side-by-side comparison
      d. Label axes: Sentiment Type vs Number of Reviews

18. END
```

---

### Key Components

| Component                | Description                                              |
|--------------------------|----------------------------------------------------------|
| **Data Sources**         | YouTube API, Google Play Scraper (JioHotstar, Netflix)   |
| **Text Cleaning**        | Regex-based (URL, HTML, symbol removal)                  |
| **Sentiment Engine**     | TextBlob polarity scoring                                |
| **Visualization**        | Word clouds (per sentiment), bar charts, comparison plot |
| **Output Files**         | youtube_comments.csv/json, df_hotstar.csv, df_netflix.csv|

### Data Flow

```
YouTube API ──→ Raw Comments ──→ Clean Text ──→ Sentiment ──→ Word Cloud
                                                              + Bar Chart

Play Store  ──→ App Reviews ──→ Clean Text ──→ Polarity ──→ Sentiment
                                                        ──→ Comparison Chart
```
