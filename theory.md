# Social Media Analytics — Viva Questions & Answers

---

## Module 1: Social Media Analytics — An Overview
**Reference: T1 — Chapter 1**

---

### Q1. What is Social Media Analytics (SMA)?
**A:** Social Media Analytics is the process of collecting, measuring, analyzing, and interpreting data from social media platforms to understand user behavior, trends, and sentiments. It helps organizations make data-driven decisions.
*Example: A brand analyzing Twitter mentions to understand customer feedback after a product launch.*

---

### Q2. What are the core characteristics of social media?
**A:**
1. **User Generated Content (UGC)** — Users create and share content
2. **Participation** — Anyone can contribute
3. **Community** — Users form groups around shared interests
4. **Openness** — Content is publicly accessible
5. **Conversation** — Two-way communication (unlike traditional media)
6. **Connectedness** — Users are linked through networks

---

### Q3. What are the different types of social media?
**A:**
| Type | Examples | Purpose |
|------|----------|---------|
| Social Networking | Facebook, LinkedIn | Connect with people |
| Microblogging | Twitter, Threads | Short-form content sharing |
| Media Sharing | YouTube, Instagram | Share photos/videos |
| Discussion Forums | Reddit, Quora | Q&A and discussions |
| Bookmarking | Pinterest, Pocket | Save and share content |
| Blogging | WordPress, Medium | Long-form content |
| Messaging | WhatsApp, Telegram | Private communication |

---

### Q4. What is the social media landscape?
**A:** The social media landscape refers to the entire ecosystem of platforms, tools, technologies, and user behaviors that make up the social media environment. It includes major platforms (Facebook, X/Twitter, YouTube, Instagram, LinkedIn), emerging platforms, and the infrastructure (APIs, algorithms, advertising systems) that supports them.

---

### Q5. Why is Social Media Analytics needed?
**A:**
- **Customer Insight** — Understand what customers think and feel
- **Brand Monitoring** — Track brand reputation in real-time
- **Competitive Analysis** — Monitor competitors' social presence
- **Marketing ROI** — Measure effectiveness of social campaigns
- **Crisis Management** — Detect and respond to negative trends early
- **Product Development** — Gather feedback for new features

---

### Q6. How is SMA used in small vs large organizations?
**A:**

| Aspect | Small Organizations | Large Organizations |
|--------|--------------------|--------------------|
| **Budget** | Limited, use free tools | Dedicated analytics teams |
| **Tools** | Google Analytics, Hootsuite | Brandwatch, Sprinklr, custom dashboards |
| **Focus** | Brand awareness, local engagement | Global campaigns, multi-platform analysis |
| **Data Volume** | Low, manageable manually | High, requires automation & ML |
| **Decision Speed** | Fast, direct | Slower, multi-level approvals |

---

### Q7. What is the purpose of Social Media Analytics?
**A:**
1. Monitor brand reputation
2. Measure campaign performance
3. Identify trending topics
4. Understand audience demographics
5. Improve customer service
6. Detect crises early
7. Support business strategy decisions

---

### Q8. Differentiate Social Media Analytics vs Traditional Business Analytics.
**A:**

| Feature | Social Media Analytics | Traditional Business Analytics |
|---------|----------------------|-------------------------------|
| **Data Source** | Social platforms (Twitter, FB) | Internal databases (CRM, ERP) |
| **Data Type** | Unstructured (text, images, video) | Structured (tables, numbers) |
| **Speed** | Real-time, streaming | Batch processing |
| **Volume** | Massive, continuous | Fixed, periodic |
| **Analysis** | NLP, sentiment, network analysis | SQL, statistical modeling |
| **Feedback Loop** | Immediate public response | Delayed surveys/reports |

---

### Q9. What are the Seven Layers of Social Media Analytics?
**A:**
1. **Identity** — Who is the user? (profile, demographics)
2. **Conversations** — What are they talking about?
3. **Actions** — What are they doing? (likes, shares, clicks)
4. **Content** — What content are they creating/consuming?
5. **Networks** — Who are they connected to?
6. **Location** — Where are they?
7. **Time** — When did they act?

---

### Q10. What are the types of Social Media Analytics?
**A:**
1. **Descriptive Analytics** — What happened? (dashboards, reports)
2. **Diagnostic Analytics** — Why did it happen? (drill-down analysis)
3. **Predictive Analytics** — What will happen? (trend forecasting)
4. **Prescriptive Analytics** — What should we do? (recommendations)

---

### Q11. Explain the Social Media Analytics Cycle.
**A:**
```
Define Goals → Identify Metrics → Collect Data → Clean & Store Data
      ↑                                                    ↓
  Refine Strategy ← Interpret Results ← Analyze Data ←────┘
```
1. **Define Goals** — What do we want to learn?
2. **Identify Metrics** — KPIs (likes, shares, sentiment)
3. **Collect Data** — APIs, web scraping
4. **Clean & Store** — Remove noise, store in databases
5. **Analyze** — Apply NLP, statistical, or network analysis
6. **Interpret** — Draw insights and conclusions
7. **Report & Refine** — Present findings, adjust strategy

---

### Q12. What are the challenges to Social Media Analytics?
**A:**
1. **Data Volume** — Massive amounts of data generated every second
2. **Data Quality** — Spam, bots, fake accounts
3. **Unstructured Data** — Text, images, videos are hard to parse
4. **Privacy Concerns** — GDPR, user consent issues
5. **Real-time Processing** — Need for low-latency analysis
6. **Platform Changes** — APIs and algorithms change frequently
7. **Multilingual Content** — Different languages and slang
8. **Sarcasm & Context** — Hard to detect true sentiment
9. **Ethical Issues** — Surveillance, manipulation concerns

---

### Q13. Name some Social Media Analytics tools.
**A:**

| Tool | Purpose |
|------|---------|
| **Google Analytics** | Website traffic from social |
| **Hootsuite** | Social media management & analytics |
| **Sprout Social** | Engagement & reporting |
| **Brandwatch** | Social listening & sentiment |
| **Buffer** | Scheduling & analytics |
| **Meltwater** | Media monitoring |
| **Talkwalker** | Social listening & analytics |
| **Twitter API** | Direct data access |
| **Facebook Graph API** | Page & post analytics |

---

## Module 2: Social Network Structure, Measures & Visualization
**Reference: T2 — Ch 3, 4, 5, 6 | T1 — Ch 4**

---

### Q14. What is a social network?
**A:** A social network is a structure made up of individuals or organizations (nodes) connected by relationships or interactions (edges). It represents how people are linked through friendships, followings, collaborations, or communications.
*Example: A Twitter follower network where each user is a node and a "follows" relationship is an edge.*

---

### Q15. What are nodes, edges, and ties?
**A:**
- **Nodes (Vertices)** — Individual entities in the network (users, pages, organizations)
- **Edges (Links)** — Connections between nodes (friendship, follow, mention)
- **Ties** — The nature/strength of the relationship between nodes
  - **Strong ties** — Close relationships (family, close friends)
  - **Weak ties** — Acquaintances, casual connections

---

### Q16. What is Degree Distribution?
**A:** Degree distribution is the probability distribution of the number of connections (edges) each node has across the entire network. It shows how connectivity is spread.
- In social networks, degree distribution often follows a **power law** — a few nodes (influencers) have very high degree, most have low degree.
*Example: On Instagram, a celebrity has millions of followers while most users have a few hundred.*

---

### Q17. What is Network Density?
**A:** Density measures how many actual edges exist compared to the maximum possible edges.
```
Density = 2E / (N × (N-1))
```
Where E = number of edges, N = number of nodes.
- Density ranges from 0 (no connections) to 1 (everyone connected)
- A dense network has many connections; a sparse network has few.

---

### Q18. What is Network Connectivity?
**A:** Connectivity refers to how easily information can flow through a network.
- **Connected graph** — Every node can reach every other node
- **Disconnected graph** — Some nodes are isolated
- **Connected components** — Subgroups that are internally connected but not to each other

---

### Q19. What is Centralization?
**A:** Centralization measures how much the network revolves around a single or few central nodes.
- **High centralization** — One or few nodes control the network (star topology)
- **Low centralization** — Power/connections are distributed evenly
*Example: A company CEO is a central node — all communication flows through them.*

---

### Q20. What is Tie Strength?
**A:** Tie strength refers to the closeness of a relationship between two nodes.
- **Strong ties** — Frequent interaction, emotional closeness (family, best friends)
- **Weak ties** — Infrequent, casual (acquaintances)
- **Granovetter's Strength of Weak Ties theory** — Weak ties are important for accessing new information and opportunities.

---

### Q21. What is Trust in social networks?
**A:** Trust is the degree to which one node relies on another for accurate information or positive interaction. In social networks:
- Trust can be **explicit** (ratings, reviews) or **implicit** (frequency of interaction)
- Trust propagation — If A trusts B and B trusts C, A may indirectly trust C
*Example: On LinkedIn, endorsements serve as trust signals.*

---

### Q22. What are Graph Layouts in network visualization?
**A:** Graph layouts determine how nodes are positioned in a visual representation:
| Layout | Description |
|--------|-------------|
| **Force-directed** | Nodes repel each other, edges attract (spring model) |
| **Circular** | Nodes placed on a circle |
| **Hierarchical** | Tree-like top-down structure |
| **Grid** | Nodes on a regular grid |
| **Geographic** | Nodes placed by real-world coordinates |

---

### Q23. How do you visualize network features?
**A:**
- **Node size** — Proportional to centrality or degree
- **Node color** — Different colors for different communities/roles
- **Edge thickness** — Proportional to tie strength or weight
- **Edge color** — Different relationship types
- **Labels** — Node names or IDs
- **Clusters** — Highlight community structures

---

### Q24. What are scale issues in network visualization?
**A:**
- **Small networks** (< 50 nodes) — Easy to visualize directly
- **Medium networks** (50-1000) — Require layout algorithms
- **Large networks** (> 1000) — Need aggregation, sampling, or interactive tools
- Problems: overlapping nodes, cluttered edges, unreadable labels

---

### Q25. What are common social media network types?
**A:**
1. **Friendship networks** — Facebook friends
2. **Follower networks** — Twitter/Instagram followers
3. **Communication networks** — Email, messaging
4. **Collaboration networks** — Co-authorship, teamwork
5. **Information networks** — Retweet, sharing chains
6. **Affiliation networks** — Users belonging to groups/pages

---

### Q26. What are common network terminologies?
**A:**
| Term | Meaning |
|------|---------|
| **Path** | Sequence of edges connecting two nodes |
| **Distance** | Shortest path between two nodes |
| **Diameter** | Longest shortest path in the network |
| **Cluster/Clique** | Dense subgroup where everyone is connected |
| **Bridge** | Edge connecting two otherwise separate groups |
| **Hub** | Node with unusually high connections |
| **Isolate** | Node with no connections |
| **Component** | Maximally connected subgraph |

---

### Q27. Name some network analytics tools.
**A:**
| Tool | Description |
|------|-------------|
| **Gephi** | Open-source network visualization |
| **NetworkX** | Python library for graph analysis |
| **Cytoscape** | Biological and social network analysis |
| **NodeXL** | Excel plugin for network graphs |
| **igraph** | R and Python graph library |
| **Neo4j** | Graph database |

---

## Module 3: Social Media Text, Action & Hyperlink Analytics
**Reference: T1 — Ch 3, 5, 7**

---

### Q28. What is Social Media Text Analytics?
**A:** Text analytics is the process of extracting meaningful information from unstructured text data on social media. It involves cleaning, processing, and analyzing text to discover patterns, sentiments, and topics.

---

### Q29. What are the types of social media text?
**A:**
1. **Posts/Tweets** — Original content shared by users
2. **Comments** — Replies to posts
3. **Reviews** — Product/service feedback
4. **Messages** — Private conversations
5. **Captions** — Text accompanying media
6. **Bios** — User profile descriptions
7. **Hashtags** — Categorical labels (#AI, #MachineLearning)

---

### Q30. What is the purpose of text analytics?
**A:**
- Sentiment analysis (positive/negative/neutral)
- Topic detection (what people are talking about)
- Trend identification (emerging themes)
- Opinion mining (what people think about a product)
- Spam/fake content detection
- Brand monitoring

---

### Q31. What are the steps in text analytics?
**A:**
```
Data Collection → Text Cleaning → Tokenization → Stopword Removal
       ↓
Stemming/Lemmatization → Feature Extraction → Analysis → Visualization
```
1. **Data Collection** — Gather text from APIs/scraping
2. **Text Cleaning** — Remove URLs, HTML, special characters
3. **Tokenization** — Split text into individual words/tokens
4. **Stopword Removal** — Remove common words (the, is, at)
5. **Stemming/Lemmatization** — Reduce words to root form
6. **Feature Extraction** — Convert to numerical features (TF-IDF, Bag of Words, Word Embeddings)
7. **Analysis** — Apply NLP models (sentiment, classification, topic modeling)
8. **Visualization** — Word clouds, frequency charts

---

### Q32. Name some text analysis tools.
**A:**
| Tool | Description |
|------|-------------|
| **NLTK** | Python NLP library |
| **spaCy** | Industrial-strength NLP |
| **TextBlob** | Simple sentiment analysis |
| **VADER** | Rule-based sentiment for social media |
| **Gensim** | Topic modeling (LDA) |
| **MonkeyLearn** | No-code text analysis |

---

### Q33. What is Social Media Action Analytics?
**A:** Action analytics analyzes the behavioral actions users perform on social media — not what they say, but what they do.
*Example: Tracking how many users liked, shared, or clicked on a post.*

---

### Q34. What are common social media actions?
**A:**
| Action | Platform | Description |
|--------|----------|-------------|
| **Like/React** | Facebook, Instagram | Show appreciation |
| **Share/Retweet** | Twitter, Facebook | Distribute content |
| **Comment** | All platforms | Respond to content |
| **Click** | All platforms | Visit a link |
| **Follow/Subscribe** | YouTube, Twitter | Subscribe to updates |
| **Save/Bookmark** | Instagram, Pinterest | Save for later |
| **Reply** | Twitter, Reddit | Direct response |
| **Mention** | Twitter, Instagram | Tag another user |
| **Hashtag use** | Twitter, Instagram | Categorize content |

---

### Q35. What are action analytics tools?
**A:**
- **Facebook Insights** — Page and post engagement metrics
- **Twitter Analytics** — Tweet impressions, engagements
- **YouTube Studio** — Watch time, likes, subscribers
- **Google Analytics** — Social referral traffic
- **Sprout Social** — Cross-platform engagement tracking

---

### Q36. What is Social Media Hyperlink Analytics?
**A:** Hyperlink analytics studies the links shared on social media — who links to whom, what content is being referenced, and how information flows through shared URLs.

---

### Q37. What are the types of hyperlinks?
**A:**
1. **Explicit links** — Direct URLs shared in posts (https://example.com)
2. **Implicit links** — Embedded in media or auto-generated previews
3. **Shortened links** — bit.ly, t.co (trackable)
4. **Deep links** — Link to specific content within an app
5. **Backlinks** — Links pointing to a website from external sources

---

### Q38. What are the types of hyperlink analytics?
**A:**
1. **Link popularity analysis** — How often a URL is shared
2. **Click-through analysis** — How many users clicked the link
3. **Referral analysis** — Which platforms drive the most traffic
4. **Anchor text analysis** — What text is used to describe the link
5. **Network analysis** — How links form a web of references

---

### Q39. What are hyperlink analytics tools?
**A:**
| Tool | Description |
|------|-------------|
| **Bitly** | Link shortening & click tracking |
| **Google Analytics** | Referral traffic analysis |
| **Ahrefs** | Backlink analysis |
| **Moz Link Explorer** | Link profile analysis |
| **BuzzSumo** | Most shared content analysis |

---

## Module 4: Social Media Location & Search Engine Analytics
**Reference: T1 — Ch 8, 9**

---

### Q40. What is Location Analytics?
**A:** Location analytics is the process of analyzing geographic data from social media to understand where users are, what they do in specific locations, and how location influences behavior and sentiment.
*Example: A restaurant chain analyzing geo-tagged Instagram posts to find which locations get the most positive reviews.*

---

### Q41. What are the sources of location data?
**A:**
1. **GPS coordinates** — From mobile devices
2. **Geo-tagged posts** — Users tag locations in posts
3. **Check-ins** — Facebook check-ins, Foursquare
4. **IP addresses** — Approximate location from internet connection
5. **Wi-Fi/Cell tower** — Triangulation-based location
6. **User profiles** — Self-reported city/country
7. **Location hashtags** — #Mumbai, #NewYork

---

### Q42. What are the categories of location analytics?
**A:**
1. **Descriptive** — Where are users? (heat maps, distribution)
2. **Spatial** — What is happening where? (geo-sentiment analysis)
3. **Temporal-Spatial** — How does location change over time? (movement patterns)
4. **Predictive** — Where will trends emerge? (location forecasting)

---

### Q43. What are the privacy concerns with location analytics?
**A:**
- **Tracking without consent** — Collecting location data unknowingly
- **Stalking risks** — Real-time location can enable harassment
- **Data breaches** — Location data exposed in hacks
- **Profiling** — Targeting users based on visited locations
- **Regulatory compliance** — GDPR, CCPA require explicit consent
- **De-anonymization** — Location data can identify individuals even without names

---

### Q44. What are location analytics tools?
**A:**
| Tool | Description |
|------|-------------|
| **Google Maps API** | Geocoding, place data |
| **GeoPandas** | Python geospatial analysis |
| **Foursquare API** | Venue and check-in data |
| **ArcGIS** | Enterprise GIS platform |
| **Mapbox** | Custom map visualization |
| **Carto** | Location intelligence platform |

---

### Q45. What is a Search Engine?
**A:** A search engine is a software system that searches the internet for web pages matching a user's query and returns ranked results.
*Examples: Google, Bing, Yahoo, DuckDuckGo.*

---

### Q46. What are the types of search engines?
**A:**
| Type | Description | Example |
|------|-------------|---------|
| **Crawler-based** | Automatically indexes web pages | Google, Bing |
| **Human-powered** | Directory-based, manually curated | DMOZ (defunct) |
| **Hybrid** | Combines both approaches | Yahoo |
| **Metasearch** | Aggregates results from multiple engines | DuckDuckGo |
| **Social search** | Ranks based on social signals | Twitter Search |

---

### Q47. What is Search Engine Analytics?
**A:** Search engine analytics involves analyzing how users find content through search engines — what keywords they use, how they click, and how social media content ranks in search results.
- **SEO analytics** — Optimizing content to rank higher
- **SEM analytics** — Measuring paid search campaigns
- **Social search analytics** — How social content appears in search

---

### Q48. What are search engine analytics tools?
**A:**
| Tool | Description |
|------|-------------|
| **Google Search Console** | Search performance, indexing |
| **Google Analytics** | Traffic sources, user behavior |
| **SEMrush** | Keyword research, competitor analysis |
| **Ahrefs** | Backlink and keyword analysis |
| **Moz** | SEO metrics and rankings |
| **Screaming Frog** | Technical SEO crawling |

---

## Module 5: Social Information Filtering
**Reference: T2 — Ch 13**

---

### Q49. What is Social Information Filtering?
**A:** Social information filtering is the process of using social signals (likes, shares, ratings, recommendations) to filter and rank content for users. Instead of relying solely on algorithms, it leverages collective user behavior.
*Example: YouTube's "Recommended for You" based on what similar users watched.*

---

### Q50. What is Social Sharing and Filtering?
**A:** Social sharing is the act of distributing content through social networks. Social filtering uses the collective actions of users to determine what content is relevant or popular.
- **Explicit filtering** — Users directly recommend/rate content
- **Implicit filtering** — Algorithm infers preference from behavior (clicks, time spent)

---

### Q51. What are Automated Recommendation Systems?
**A:** Systems that automatically suggest content, products, or connections to users based on data analysis.

| Type | Method | Example |
|------|--------|---------|
| **Content-based** | Recommends similar items based on features | Spotify suggesting similar songs |
| **Collaborative filtering** | Recommends what similar users liked | Amazon's "Customers also bought" |
| **Hybrid** | Combines both approaches | Netflix recommendations |

---

### Q52. Differentiate Traditional vs Social Recommendation Systems.
**A:**

| Feature | Traditional | Social |
|---------|-------------|--------|
| **Data Source** | User ratings, purchase history | Social interactions, friends' activity |
| **Cold Start** | Problem with new users | Mitigated by social connections |
| **Transparency** | Black box | Users see why (friend X liked this) |
| **Trust** | Algorithm-based | Trust-based (friend recommendations) |
| **Scalability** | Scales well | Depends on social graph density |
| **Example** | Netflix collaborative filtering | Facebook's "Pages you may like" |

---

### Q53. What is Social Media and Business Alignment?
**A:** It refers to how an organization's social media activities align with its overall business goals and strategy.
- **Brand awareness** — Increase visibility
- **Lead generation** — Drive potential customers
- **Customer retention** — Engage existing customers
- **Revenue** — Direct sales through social commerce
- **Reputation management** — Maintain positive brand image

---

### Q54. What are Social Media KPIs (Key Performance Indicators)?
**A:**

| KPI Category | Metrics |
|--------------|---------|
| **Awareness** | Impressions, reach, follower count |
| **Engagement** | Likes, comments, shares, saves |
| **Conversion** | Click-through rate, sign-ups, purchases |
| **Advocacy** | Mentions, positive sentiment, reviews |
| **Customer Service** | Response time, resolution rate |

---

### Q55. How do you formulate a Social Media Strategy?
**A:**
1. **Set Goals** — SMART goals (Specific, Measurable, Achievable, Relevant, Time-bound)
2. **Identify Audience** — Demographics, interests, platforms
3. **Choose Platforms** — Where does the target audience spend time?
4. **Content Plan** — What to post, when, how often
5. **Engagement Plan** — How to respond, interact
6. **Budget** — Paid ads, tools, team
7. **Measure & Adjust** — Track KPIs, refine based on data

---

### Q56. What are the risks of social media for businesses?
**A:**
1. **Reputation damage** — Negative viral content
2. **Data breaches** — Leaked customer data
3. **Legal issues** — Copyright, defamation, compliance
4. **Employee misuse** — Inappropriate posts by staff
5. **Fake news** — Misinformation spreading about brand
6. **Platform dependency** — Algorithm changes reduce reach
7. **Troll/attack campaigns** — Coordinated negative attacks

---

### Q57. How do you manage social media risks?
**A:**
- **Social media policy** — Clear guidelines for employees
- **Monitoring tools** — Real-time alerts for negative mentions
- **Crisis management plan** — Predefined response protocols
- **Access control** — Limit who can post on official accounts
- **Legal compliance** — Follow platform rules and regulations
- **Regular audits** — Review social media activity periodically

---

## Module 6: Social Media Analytics Applications and Privacy
**Reference: T2 — Ch 13**

---

### Q58. How is social media used in the public sector?
**A:**
1. **Government communication** — Official announcements, policy updates
2. **Emergency management** — Disaster alerts, evacuation info
3. **Public engagement** — Citizen feedback, polls
4. **Law enforcement** — Crime monitoring, investigation
5. **Health monitoring** — Disease outbreak tracking (e.g., COVID-19 trends)
6. **Election campaigns** — Voter outreach, sentiment tracking

---

### Q59. How do you analyze public sector social media?
**A:**
- **Sentiment analysis** — Public opinion on policies
- **Topic modeling** — What issues citizens care about
- **Engagement metrics** — How many citizens interact
- **Reach analysis** — How far government messages spread
- **Crisis detection** — Early warning signals
*Example: Analyzing tweets during a natural disaster to identify affected areas.*

---

### Q60. How do you analyze individual users on social media?
**A:**
- **Profile analysis** — Demographics, interests, influence
- **Behavior analysis** — Posting frequency, active times
- **Content analysis** — What they share, topics of interest
- **Network analysis** — Who they interact with
- **Sentiment patterns** — Emotional tendencies
- **Bot detection** — Identifying automated accounts

---

### Q61. How is social media used in business?
**A:**
1. **Marketing** — Brand promotion, advertising campaigns
2. **Customer service** — Responding to queries/complaints
3. **Sales** — Social commerce, lead generation
4. **Market research** — Understanding customer needs
5. **Competitive intelligence** — Monitoring competitors
6. **Recruitment** — LinkedIn hiring, employer branding
7. **Product development** — Gathering user feedback

---

### Q62. How do you measure success in business social media?
**A:**
| Metric | What It Measures |
|--------|-----------------|
| **Engagement Rate** | (Likes + Comments + Shares) / Reach × 100 |
| **Click-Through Rate** | Clicks / Impressions × 100 |
| **Conversion Rate** | Conversions / Clicks × 100 |
| **Customer Acquisition Cost** | Total spend / New customers |
| **Return on Investment** | (Revenue - Cost) / Cost × 100 |
| **Net Promoter Score** | Customer loyalty metric |
| **Share of Voice** | Brand mentions / Total industry mentions |

---

### Q63. What is social media interaction and monitoring?
**A:**
- **Interaction** — Actively engaging with users (replying, liking, commenting)
- **Monitoring** — Passively tracking mentions, keywords, and trends without direct engagement
- **Social Listening** — Understanding broader conversations and sentiment around a brand/industry
*Tools: Hootsuite, Brandwatch, Mention, Sprout Social*

---

### Q64. What is Privacy in the context of social media?
**A:** Privacy refers to the right of users to control what personal information is collected, shared, and used on social media platforms.
- **Data minimization** — Collect only what's needed
- **User consent** — Explicit permission before data collection
- **Transparency** — Clear privacy policies
- **Right to be forgotten** — Users can request data deletion

---

### Q65. What are privacy policies in social media?
**A:** Privacy policies are legal documents that explain:
1. What data is collected (name, location, behavior)
2. How data is used (advertising, analytics, third-party sharing)
3. How data is stored and protected
4. User rights (access, delete, opt-out)
5. Cookie usage and tracking
*Example: Facebook's Data Policy explains how user data is used for ad targeting.*

---

### Q66. What is data ownership in social media?
**A:** Data ownership refers to who has rights over the content and data generated on social media.
- **User-created content** — Generally owned by the user, but platforms get a license to use it
- **Platform data** — Owned by the platform (algorithms, aggregated data)
- **Derived data** — Analytics insights may be owned by the analyzer
- **Key issue** — Users often don't realize they grant platforms broad usage rights when they sign up

---

### Q67. How can users maintain privacy online?
**A:**
1. **Review privacy settings** — Limit who sees your posts
2. **Be cautious with personal info** — Don't share address, phone number
3. **Use strong passwords** — Unique passwords for each platform
4. **Enable 2FA** — Two-factor authentication
5. **Review app permissions** — Revoke access for unused apps
6. **Be aware of phishing** — Don't click suspicious links
7. **Use VPN** — Mask your IP address
8. **Regularly audit** — Check what data platforms have on you

---

## Quick Reference: Key Formulas

| Metric | Formula |
|--------|---------|
| **Network Density** | `2E / (N × (N-1))` |
| **Degree Centrality** | `degree(node) / (N-1)` |
| **Engagement Rate** | `(Likes + Comments + Shares) / Reach × 100` |
| **Click-Through Rate** | `Clicks / Impressions × 100` |
| **Sentiment Polarity** | `TextBlob(text).sentiment.polarity` (range: -1 to +1) |
| **Betweenness Centrality** | Fraction of shortest paths passing through a node |
| **Closeness Centrality** | `(N-1) / Sum of shortest paths to all other nodes` |
