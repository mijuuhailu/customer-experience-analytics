# Fintech Review Analytics

A real-world data engineering and NLP project focused on analyzing Google Play Store reviews for major Ethiopian banking applications.

## Project Overview

This project was developed as part of a fintech analytics challenge for Omega Consultancy. The goal is to collect, preprocess, analyze, and visualize customer reviews from Ethiopian mobile banking applications in order to generate actionable business insights.

The analysis focuses on three Ethiopian banks:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The project aims to help product teams understand:

- Common customer complaints
- User satisfaction drivers
- Feature requests
- Sentiment trends
- Areas requiring product improvement

---

# Objectives

## Task 1 — Data Collection and Preprocessing

The objective of this phase is to:

- Scrape reviews from the Google Play Store
- Clean and preprocess the data
- Store the dataset in CSV format
- Manage the project using Git and GitHub best practices

---

# Technologies Used

- Python
- Pandas
- NumPy
- google-play-scraper
- Git & GitHub
- GitHub Actions (CI/CD)

---

# Project Structure

```bash
fintech-review-analytics/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── data/
│
├── notebooks/
│
├── src/
│   ├── scrape_reviews.py
│   └── preprocess.py
│
├── tests/
│
├── .gitignore
├── README.md
├── requirements.txt
```

---

# Data Source

The data was collected from the Google Play Store using the `google-play-scraper` Python package.

Source:
- Google Play Store reviews

---

# Banks and Applications

| Bank | App ID |
|---|---|
| CBE | `com.combanketh.mobilebanking` |
| BOA | `com.boa.boaMobileBanking` |
| Dashen | `com.dashen.dashensuperapp` |

---

# Data Collection Methodology

Reviews were scraped using the `reviews()` function from the `google-play-scraper` library.

The following information was collected:

- Review text
- Rating (1–5)
- Review date
- Bank name
- Source platform

### Scraping Configuration

- Language: English (`lang='en'`)
- Country: Ethiopia (`country='et'`)
- Sorting: Newest reviews
- Target: 400+ reviews per bank

---

# Preprocessing Steps

The preprocessing pipeline performs the following operations:

1. Remove duplicate reviews
2. Drop rows with missing review text or ratings
3. Normalize date format to `YYYY-MM-DD`
4. Save cleaned dataset as CSV

Final dataset columns:

| Column | Description |
|---|---|
| review | User review text |
| rating | Star rating |
| date | Review date |
| bank | Bank name |
| source | Data source |

---

# Output

The cleaned dataset is saved locally as:

```bash
data/cleaned_reviews.csv
```

Note:
The `data/` directory and CSV files are excluded from Git tracking using `.gitignore`.

---


---

# Limitations

- Some applications may return fewer reviews depending on Google Play availability.
- Google Play may enforce rate limits during scraping.
- Some reviews may contain mixed languages or incomplete text.
- Historical reviews may be limited by the scraper API.

---

# Future Improvements

- Sentiment analysis using DistilBERT
- Theme extraction using TF-IDF and spaCy
- PostgreSQL database integration
- Interactive dashboards and visualizations
- Automated testing pipeline

---

