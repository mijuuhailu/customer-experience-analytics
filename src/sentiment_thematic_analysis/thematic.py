# scripts/sentiment_thematic_analysis/thematic.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

import os

def extract_top_ngrams(df, text_column='review', bank_column='bank', ngram_range=(1, 2), top_n=20, output_dir=None):
    banks = df[bank_column].unique()
    result = {}

    for bank in banks:
        print(f"\n🔍 Top {top_n} keywords for: {bank}")
        reviews = df[df[bank_column] == bank][text_column].dropna().astype(str)
        
        vectorizer = TfidfVectorizer(stop_words='english', ngram_range=ngram_range, max_features=1000)
        tfidf_matrix = vectorizer.fit_transform(reviews)
        feature_names = vectorizer.get_feature_names_out()
        scores = tfidf_matrix.sum(axis=0).A1
        keywords_scores = list(zip(feature_names, scores))

        top_keywords = sorted(keywords_scores, key=lambda x: x[1], reverse=True)[:top_n]
        result[bank] = top_keywords

        # Print the keywords to console
        for keyword, score in top_keywords:
            print(f"{keyword:<25} {score:.2f}")

        # Optionally save to CSV
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            out_path = os.path.join(output_dir, f"top_keywords_{bank}.csv")
            pd.DataFrame(top_keywords, columns=['keyword', 'score']).to_csv(out_path, index=False)
            print(f"\n Saved top keywords for {bank} to: {out_path}")

    return result

def run_sklearn_lda(df, text_column='review', bank_column='bank', n_topics=5, n_top_words=10, max_features=1000):
    reviews = df[text_column].dropna().astype(str)
    bank_name = df[bank_column].iloc[0] if bank_column in df.columns else "App"

    vectorizer = TfidfVectorizer(stop_words='english', max_features=max_features)
    tfidf = vectorizer.fit_transform(reviews)

    lda = LatentDirichletAllocation(n_components=n_topics, random_state=42, learning_method='online')
    lda.fit(tfidf)

    feature_names = vectorizer.get_feature_names_out()
    print(f"\n Topics for: {bank_name}")
    for idx, topic in enumerate(lda.components_):
        top_indices = topic.argsort()[:-n_top_words - 1:-1]
        top_words = [feature_names[i] for i in top_indices]
        print(f"Topic {idx + 1}: {' | '.join(top_words)}")

    return vectorizer, lda



def group_topics_into_themes(df, lda_model, vectorizer, bank_name, top_n_words=10):
    feature_names = vectorizer.get_feature_names_out()
    topic_words = []

    print(f"\n Grouping Topics for: {bank_name}")

    # Step 1: Extract top words per topic
    for idx, topic in enumerate(lda_model.components_):
        top_indices = topic.argsort()[:-top_n_words - 1:-1]
        words = [feature_names[i] for i in top_indices]
        topic_words.append(words)
        print(f"Topic {idx + 1}: {', '.join(words)}")

    # Step 2: Manually define rules to cluster into themes
  
        themes = {
        "Account Access Issues": [],
        "Transaction Performance": [],
        "User Interface & Experience": [],
        "Customer Support": [],
        "Feature Requests": []
    }

    # Step 3: Assign topic words to themes based on keyword matching
    for i, words in enumerate(topic_words):
        topic_label = f"Topic {i+1}"

        for word in words:
            lw = word.lower()
            
            if any(k in lw for k in [
                "login", "log", "password", "access", "fail", "blocked", "reset", "credential"
            ]):
                themes["Account Access Issues"].append((topic_label, word))

            elif any(k in lw for k in [
                "transfer", "send", "receive", "delay", "process", "slow", "speed", "time", "pending", "transaction", "loading"
            ]):
                themes["Transaction Performance"].append((topic_label, word))

            elif any(k in lw for k in [
                "design", "layout", "easy", "ui", "interface", "look", "navigation", "friendly", "simple", "beautiful", "responsive", "intuitive"
            ]):
                themes["User Interface & Experience"].append((topic_label, word))
            
            elif any(k in lw for k in [
                "support", "help", "call", "service", "agent", "response", "assistance", "staff", "contact", "feedback"
            ]):
                themes["Customer Support"].append((topic_label, word))

            elif any(k in lw for k in [
                "add", "feature", "option", "setting", "notification", "update", "custom", "improve", "enable", "disable"
            ]):
                themes["Feature Requests"].append((topic_label, word))

       

    # Step 4: Print result
    for theme, entries in themes.items():
        if entries:
            print(f"\n {theme}:")
            keywords = [kw for _, kw in entries]
            print(", ".join(set(keywords)))

    return themes
