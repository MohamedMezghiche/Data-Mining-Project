# 02 — News Headlines Analyzer

Goal: collect headlines from multiple permitted news sources, preprocess the text, and analyze word frequencies.

Suggested workflow:
1. Choose news RSS feeds or APIs that permit use.
2. Collect headline, source, URL, publication date, and collection timestamp.
3. Save raw records under `data/raw/`.
4. Normalize and preprocess headlines.
5. Calculate word frequencies and compare sources or dates.
6. Visualize and discuss limitations, including source and language bias.

Expected CSV columns: `headline`, `source`, `url`, `published_at`, `collected_at`.
