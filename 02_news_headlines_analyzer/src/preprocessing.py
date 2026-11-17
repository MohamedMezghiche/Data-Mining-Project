"""Basic headline text preprocessing."""
import re

def preprocess_headline(text: str) -> list[str]:
    text = text.lower()
    text = re.sub(r"https?://\\S+|[^a-z0-9\\s]", " ", text)
    return [word for word in text.split() if len(word) > 2]
