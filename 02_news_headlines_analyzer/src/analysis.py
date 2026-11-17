"""Word-frequency analysis for news headlines."""
from collections import Counter
import pandas as pd
from preprocessing import preprocess_headline

def word_frequencies(df: pd.DataFrame) -> pd.Series:
    if "headline" not in df.columns:
        raise ValueError("Expected a 'headline' column.")
    words = []
    for headline in df["headline"].dropna().astype(str):
        words.extend(preprocess_headline(headline))
    return pd.Series(Counter(words)).sort_values(ascending=False)
