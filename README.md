# Data Mining Project — Foundations

Group project covering two topics:
1. Web Scraping of Job Listings
2. News Headlines Analyzer

## Setup
```bash
python -m venv .venv
```
Activate the environment:
- Windows PowerShell: `.venv\Scripts\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

Install dependencies:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Project structure
- `01_job_listings_scraper/`: collect, clean, and analyze job listing data.
- `02_news_headlines_analyzer/`: collect headlines, preprocess text, and analyze word frequency.
- `docs/`: project notes, methodology, and report materials.

## Responsible data collection
Use public pages or APIs that permit collection. Check each site's terms, robots.txt, privacy requirements, and rate limits. Prefer official APIs or RSS feeds where available. Do not bypass logins, paywalls, CAPTCHAs, or access controls.

## Team workflow
Each teammate should work on a separate branch and open a pull request before merging into `main`.
