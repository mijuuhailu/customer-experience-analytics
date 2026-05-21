from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

analyzer = SentimentIntensityAnalyzer()

def vader_sentiment(text):
    score = analyzer.polarity_scores(str(text))['compound']
    if score >= 0.05:
        return 'positive', score
    elif score <= -0.05:
        return 'negative', score
    else:
        return 'neutral', score

def apply_vader_sentiment(input_path, output_path):
    df = pd.read_csv(input_path)
    df[['sentiment', 'sentiment_score']] = df['review'].apply(vader_sentiment).apply(pd.Series)
    print(df['sentiment'].value_counts())
    df.to_csv(output_path, index=False)
    return df

def aggregate_sentiment(df, output_path=None):
    # Group by bank and rating
    agg_df = df.groupby(['bank', 'rating']).agg(
        mean_sentiment_score=('sentiment_score', 'mean'),
        review_count=('sentiment', 'count'),
        sentiment_breakdown=('sentiment', lambda x: x.value_counts().to_dict())
    ).reset_index()

    # Optional: Save to file
    if output_path:
        agg_df.to_csv(output_path, index=False)
        print(f"Aggregated sentiment saved to {output_path}")
    
    return agg_df
