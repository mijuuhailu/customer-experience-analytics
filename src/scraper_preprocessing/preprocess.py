import pandas as pd
import os
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import TreebankWordTokenizer
from nltk.stem import WordNetLemmatizer

# Download only required NLTK corpora (punkt is not needed)
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()
tokenizer = TreebankWordTokenizer()

def clean_text(text):
    # Tokenize using Treebank tokenizer (no punkt required)
    tokens = tokenizer.tokenize(text.lower())

    # Remove stopwords and non-alphabetic tokens
    tokens = [w for w in tokens if w.isalpha() and w not in stop_words]

    # Lemmatize
    lemmatized = [lemmatizer.lemmatize(w) for w in tokens]

    return " ".join(lemmatized)

def preprocess_reviews(input_path, output_path):
    df = pd.read_csv(input_path)
    print(f"Initial rows loaded: {len(df)}")

    df = df.dropna(subset=["Review Text", "Rating", "Date", "Bank/App Name", "Source"])
    print(f"Rows after dropping missing values: {len(df)}")

    df = df.drop_duplicates()
    print(f"Rows after dropping duplicates: {len(df)}")

    df["Date"] = pd.to_datetime(df["Date"]).dt.strftime('%Y-%m-%d')

    df_cleaned = df.rename(columns={
        "Review Text": "review",
        "Rating": "rating",
        "Date": "date",
        "Bank/App Name": "bank",
        "Source": "source"
    })

    print("🔄 Preprocessing reviews (tokenizing, removing stopwords, lemmatizing)...")
    df_cleaned["review"] = df_cleaned["review"].astype(str).apply(clean_text)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_cleaned.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to {output_path}")
    print(f"🧾 Final row count: {len(df_cleaned)}")
