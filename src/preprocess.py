import pandas as pd


# Load data
df = pd.read_csv("data/raw_reviews.csv")


print("Initial shape:", df.shape)


# Remove duplicates
df = df.drop_duplicates()


# Remove missing review or rating
df = df.dropna(subset=["review", "rating"])


# Normalize dates
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")


# Final check
print("Final shape:", df.shape)


# Save cleaned data
df.to_csv("data/cleaned_reviews.csv", index=False)


print("Preprocessing complete.")