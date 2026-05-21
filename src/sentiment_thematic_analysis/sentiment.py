# scripts/sentiment_analysis/sentiment_model.py

import pandas as pd
from transformers import pipeline 
import os



# Load Hugging Face sentiment classifier
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def label_sentiment(text):
    try:
        result = sentiment_pipeline(text[:512])[0]  # truncate to 512 tokens
        label = result['label']
        score = result['score']

        if label == "POSITIVE":
            return "positive", 1
        elif label == "NEGATIVE":
            return "negative", -1
    except:
        return "neutral", 0

def apply_sentiment(bank_prefix, input_dir="data/clean", output_dir="data/processed"):
    input_path = f"{input_dir}/{bank_prefix}_clean.csv"
    output_path = f"{output_dir}/sentiment_reviews_{bank_prefix}.csv"
    
    df = pd.read_csv(input_path)
    print(f"Applying sentiment to {len(df)} reviews for {bank_prefix}...")

    df[['sentiment', 'sentiment_score']] = df['review'].progress_apply(label_sentiment).apply(pd.Series)
    df.to_csv(output_path, index=False)
    print(f"Sentiment-tagged data saved to {output_path}")

    return df


def aggregate_sentiment(df, output_path="../data/processed/sentiment_aggregated.csv"):
    agg_df = df.groupby(["bank", "rating"]).agg({
        "sentiment_score": ["mean", "count"],
        "sentiment": lambda x: x.value_counts().to_dict()
    }).reset_index()

    agg_df.columns = ["bank", "rating", "mean_sentiment", "review_count", "sentiment_breakdown"]
    agg_df.to_csv(output_path, index=False)
    print(f"Aggregated sentiment saved to {output_path}")
    return agg_df


