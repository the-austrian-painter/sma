# Algorithm: Content-Based & Location-Based Social Media Analytics

## Experiment 9 — Content and Location Based SMA

---

### Part A: User Mention Extraction & Analysis

```
1. START

2. Import required libraries:
      pandas, re, matplotlib, seaborn, collections.Counter,
      geopandas, geopy (Nominatim), shapely

3. CREATE SAMPLE DATA:
      a. Define DataFrame with 'Text' column containing tweets
         with @user mentions

4. EXTRACT MENTIONS:
      FOR each text entry:
         a. Apply regex pattern: r'@\w+'
         b. Extract all matching @mentions
      Store in 'Mentions' column

5. COUNT MENTION FREQUENCIES:
      a. Flatten list of all mentions across all tweets
      b. Use Counter to count occurrences of each mention
      c. Create DataFrame with columns ['User', 'Count']
      d. Sort by Count in descending order

6. VISUALIZE TOP MENTIONS:
      a. Plot bar chart (User vs Count)
      b. Title: "Top Mentioned Users"
      c. Rotate x-axis labels by 45°

7. END (Part A)
```

---

### Part B: Geographic Distribution of Reviews

```
8. CREATE LOCATION DATA:
      a. Define DataFrame with 'Review' and 'Location' columns
         (cities: Mumbai, Delhi, New York, London, Tokyo)

9. GEOCODE LOCATIONS:
      a. Initialize Nominatim geolocator with user_agent="geo_app"
      b. FOR each location:
         - Call geolocator.geocode(location)
         - Extract (latitude, longitude)
         - Handle exceptions → return (None, None)
         - Sleep 1 second between API calls (rate limiting)
      c. Store coordinates in 'Latitude' and 'Longitude' columns

10. CREATE GEO DATAFRAME:
      a. Create Point geometry from (Longitude, Latitude) pairs
      b. Create GeoDataFrame with geometry column
      c. Drop rows with missing coordinates

11. LOAD WORLD MAP:
      a. Fetch Natural Earth 110m cultural shapefile
      b. Read as GeoDataFrame

12. PLOT GEOGRAPHIC DISTRIBUTION:
      a. Plot world map as base layer
      b. Overlay review locations as red markers
      c. Title: "Geographic Distribution of Reviews"

13. END (Part B)
```

---

### Part C: Hashtag Trend Analysis

```
14. CREATE HASHTAG DATA:
      a. Define DataFrame with 'Text' column containing tweets
         with #hashtags (e.g., #DeepLearning, #AI, #Python)

15. EXTRACT HASHTAGS:
      FOR each text entry:
         a. Apply regex pattern: r'#\w+'
         b. Extract all matching #hashtags
      Store in 'Hashtags' column

16. COUNT HASHTAG FREQUENCIES:
      a. Flatten list of all hashtags across all tweets
      b. Use Counter to count occurrences of each hashtag
      c. Create DataFrame with columns ['Hashtag', 'Count']
      d. Sort by Count in descending order

17. VISUALIZE TRENDING HASHTAGS:
      a. Plot bar chart (Hashtag vs Count)
      b. Title: "Top Trending Hashtags"
      c. Rotate x-axis labels by 45°

18. END (Part C)
```

---

### Part D: Location-Based Sentiment Analysis & Geo-Visualization

```
19. CREATE REVIEW DATA:
      a. Define DataFrame with 'Review' and 'Location' columns
         (cities: Bangalore, Pune, Chennai)

20. CLASSIFY SENTIMENT:
      FOR each review:
         a. Compute polarity = TextBlob(review).sentiment.polarity
         b. Classify:
            - polarity > 0   → "Positive"
            - polarity < 0   → "Negative"
            - polarity == 0  → "Neutral"
      Store in 'Sentiment' column

21. AGGREGATE SENTIMENT BY LOCATION:
      a. Group by ['Location', 'Sentiment']
      b. Count occurrences using size()
      c. Unstack to create location-wise sentiment matrix
      d. Fill NaN with 0

22. PLOT SENTIMENT DISTRIBUTION BY LOCATION:
      a. Plot grouped bar chart
      b. X-axis: Location, Y-axis: Count
      c. Title: "Sentiment Distribution by Location"

23. GEOCODE SENTIMENT LOCATIONS:
      a. Copy sentiment DataFrame
      b. Apply get_coordinates() to each location
      c. Store Latitude and Longitude

24. CREATE SENTIMENT GEO DATAFRAME:
      a. Create Point geometry from coordinates
      b. Create GeoDataFrame
      c. Drop rows with missing coordinates

25. PLOT WORLD MAP WITH SENTIMENT OVERLAY:
      a. Load world map (Natural Earth shapefile)
      b. Plot base world map
      c. Overlay sentiment points with color coding:
         - Positive → Green markers
         - Negative → Red markers
         - Neutral  → Blue markers
      d. Add legend for sentiment types
      e. Title: "Geographic Distribution of Sentiment Reviews"

26. PLOT ASIA-FOCUSED MAP:
      a. Filter world map for CONTINENT == 'Asia'
      b. Repeat sentiment overlay on Asia map
      c. Same color coding and legend

27. END (Part D)
```

---

### Key Components

| Component                | Description                                           |
|--------------------------|-------------------------------------------------------|
| **Content Analysis**     | Regex-based @mention and #hashtag extraction          |
| **Geocoding**            | Nominatim (OpenStreetMap) geocoder                    |
| **Geo Visualization**    | GeoPandas + Natural Earth shapefiles                  |
| **Sentiment Engine**     | TextBlob polarity scoring                             |
| **Color Coding**         | Green=Positive, Red=Negative, Blue=Neutral            |

### Data Flow

```
Text Data ──→ Regex Extraction ──→ Frequency Count ──→ Bar Chart
              (@mentions, #hashtags)

Location Data ──→ Geocoding ──→ GeoDataFrame ──→ World Map Overlay
                                                        │
                                          ┌─────────────┼─────────────┐
                                          │             │             │
                                       Positive      Negative      Neutral
                                       (Green)        (Red)        (Blue)
```
