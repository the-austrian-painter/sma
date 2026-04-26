# Algorithm: Data Cleaning, Storage & Sentiment Analysis with Word Cloud

## Experiment 3 — Data Cleaning and Storage

---

### Algorithm

```
1. START

2. Import required libraries:
      pandas, numpy, matplotlib, seaborn, nltk, textblob,
      wordcloud, sklearn (CountVectorizer, TfidfVectorizer),
      plotly, cufflinks

3. LOAD DATA:
      a. Read tweets CSV file into a pandas DataFrame (tweets_df)
      b. Display shape, head, info, and value counts for initial inspection

4. VISUALIZE MISSING VALUES:
      a. Generate heatmap of null values using seaborn
      b. Display column-wise missing value distribution

5. EXPLORE TOP LOCATIONS/AIRLINES:
      a. Count value occurrences in 'airline' column
      b. Display top 10 locations/airlines

6. REMOVE STOPWORDS:
      a. Load English stopwords from NLTK
      b. Filter out stopwords from 'text' column

7. CLEAN TEXT — REMOVE PUNCTUATIONS:
      a. Define punctuation list: ['%', '/', ':', '\\', '&amp', '&', ';', '?']
      b. FOR each text entry:
         - Replace each punctuation character with empty string
      c. Apply cleaning function to 'text' column

8. DROP EMPTY TWEETS:
      a. Replace empty strings in 'text' column with NaN
      b. Drop rows where 'text' is NaN
      c. Reset DataFrame index

9. PLOT TOP 20 MOST COMMON WORDS:
      a. Initialize CountVectorizer with extended stopwords
      b. Fit and transform 'text' column to get word counts
      c. Sum word frequencies across all documents
      d. Sort by frequency descending, take top 20
      e. Plot bar chart of word frequencies

10. GENERATE TOP BIGRAMS:
      a. Initialize CountVectorizer with ngram_range=(2, 4)
      b. Fit and transform corpus
      c. Sum bag-of-words matrix column-wise
      d. Map word indices to actual n-gram strings
      e. Sort by frequency, take top 8
      f. Plot horizontal bar chart of bigram frequencies

11. COMPUTE SUBJECTIVITY AND POLARITY (TextBlob):
      a. FOR each text entry:
         - subjectivity = TextBlob(text).sentiment.subjectivity
         - polarity     = TextBlob(text).sentiment.polarity
      b. Add 'subjectivity' and 'polarity' columns to DataFrame

12. CLASSIFY SENTIMENT:
      a. Compute textblob_score = TextBlob(text).sentiment.polarity
      b. Apply threshold (neutral_threshold = 0.05):
         - score >= 0.05           → "Positive"
         - score <= -0.05          → "Negative"
         - otherwise               → "Neutral"
      c. Store result in 'textblob_sentiment' column

13. SEGMENT DATA BY SENTIMENT:
      a. Filter positive tweets   → df_positive
      b. Filter retweeted positive tweets (retweet_count > 0) → df_very_positive
      c. Filter negative tweets   → df_negative
      d. Filter neutral tweets    → df_neutral

14. GENERATE WORD CLOUDS:
      FOR each sentiment category (positive, negative, neutral):
         a. Join all text entries into a single string
         b. Create WordCloud object (collocations=False, white background)
         c. Generate word cloud from joined text
         d. Display using matplotlib imshow with bilinear interpolation

15. END
```

---

### Key Components

| Component                | Description                                           |
|--------------------------|-------------------------------------------------------|
| **Input**                | Tweets CSV file (airline sentiment dataset)           |
| **Text Cleaning**        | Stopword removal, punctuation removal, NaN filtering  |
| **Feature Extraction**   | CountVectorizer (unigrams + bigrams), TF-IDF          |
| **Sentiment Engine**     | TextBlob (polarity + subjectivity)                    |
| **Visualization**        | Heatmap, bar charts, word clouds                      |
| **Polarity Threshold**   | ±0.05 for neutral classification                      |

### Sentiment Classification Thresholds

| Polarity Score        | Sentiment  |
|-----------------------|------------|
| `>= 0.05`             | Positive   |
| `<= -0.05`            | Negative   |
| `-0.05 < x < 0.05`   | Neutral    |
