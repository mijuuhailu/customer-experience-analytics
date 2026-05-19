import pandas as pd

# Load raw data
df = pd.read_csv("data/raw_reviews.csv")

print("Initial shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Remove missing review or rating
df = df.dropna(subset=["review", "rating"])

# Convert reviews to string
df["review"] = df["review"].astype(str)

# Remove extra spaces
df["review"] = df["review"].str.strip()

# Remove very short reviews (less than 3 words)
df = df[df["review"].str.split().str.len() >= 3]

# Normalize dates
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

print("Final shape:", df.shape)

# Save cleaned data
df.to_csv("data/cleaned_reviews.csv", index=False)

print("Preprocessing complete.")