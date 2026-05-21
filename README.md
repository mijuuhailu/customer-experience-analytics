#  Mobile Banking Review Analysis - Omega Consultancy

Omega Consultancy is spearheading a data-driven initiative to support leading banks in enhancing their mobile banking applications, with a strategic focus on improving customer satisfaction and retention. This project involves the collection and analysis of user-generated reviews from the Google Play Store for three major Ethiopian banks—Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), and Dashen Bank. Using natural language processing (NLP) techniques, the objective is to extract sentiment (positive, negative, or neutral) and identify recurring themes such as bugs, user interface issues, performance problems, and feature requests.

---

## Objectives

- Scrape user reviews from the Google Play Store for selected banking apps.

- Preprocess, clean, and standardize review data.

- Perform sentiment analysis and thematic keyword extraction.

- Identify user satisfaction drivers and pain points.

- Store cleaned data in a PostgreSQL database for long-term accessibility.

- Visualize findings and deliver actionable recommendations.
---
## Contributions
### Review Collection:
 Scraped over 1,200 user reviews from the Google Play Store across three major banks using google-play-scraper.

### Data Preprocessing:
 Standardized review datasets by removing duplicates, normalizing date formats, and handling missing values for consistency and analysis-readiness.

### Sentiment Analysis:
 Implemented VADER to classify review sentiment as positive, negative, or neutral. Originally explored transformer-based models like distilbert-base-uncased-finetuned-sst-2-english, but shifted due to performance constraints.

### Thematic Analysis:
 Used TF-IDF and keyword extraction to identify common themes such as login issues, UI satisfaction, and network performance across banks.

### Database Integration:
 Designed a PostgreSQL schema and programmatically inserted the cleaned dataset into relational tables for scalable storage and enterprise readiness.

### Insight Generation:
 Identified key satisfaction drivers and pain points, aiding targeted recommendations for mobile banking app improvements.

### Visualization:
 Created keyword clouds and bar charts to support findings and aid in stakeholder communication.

##  Methodology

### Data Collection & Preprocessing
Collected 400+ reviews per bank using google-play-scraper. Cleaned the data by removing duplicates, normalizing dates, and standardizing column names.

### Sentiment & Thematic Analysis
Applied VADER for sentiment classification. Extracted keywords using TF-IDF to group reviews into themes like UI experience, transaction issues, and feature requests.

### Database Integration
Designed and implemented a PostgreSQL database schema to store cleaned reviews, including associated metadata and sentiment scores.

### Insights & Visualization
Analyzed sentiment and theme distribution across banks. Visualized trends using bar charts and keyword clouds to support improvement recommendations.

---
## Future Plans
- Replace the VADER model with more advanced transformer-based models (e.g., distilbert-base-uncased-finetuned-sst-2-english) for improved sentiment accuracy.

- Implement unit tests to ensure code robustness and maintainability as the project scales.
--- 
## Tools Used

Python 3.10+: Core programming language.

- google-play-scraper: For scraping mobile app reviews.

- pandas / NumPy: For data cleaning, manipulation, and analysis.

- NLTK / VADER: For sentiment analysis.

- scikit-learn: For TF-IDF keyword extraction and preprocessing.

- Matplotlib / Seaborn / WordCloud: For visualizations and exploratory analysis.

- PostgreSQL: Used as the relational database to store cleaned and enriched review data.

- psycopg2 / SQLAlchemy: For database connections and SQL operations.

- Git / GitHub: For version control and collaboration.

---
## Conclusion 

This project successfully analyzed user feedback from banking apps to identify key satisfaction drivers and recurring pain points. By combining sentiment analysis with thematic keyword extraction, we surfaced actionable insights to guide app improvements. The structured pipeline and database integration ensure scalability and real-world applicability for ongoing product enhancement.

