# 01 — Web Scraping of Job Listings

Goal: collect job titles, companies, locations, and required skills from permitted public sources, then analyze in-demand skills with Pandas.

Suggested workflow:
1. Identify an allowed job-data source (prefer an official API or permitted public dataset).
2. Inspect its terms and collection rules.
3. Collect a small sample with `src/scraper.py`.
4. Save raw data under `data/raw/`.
5. Clean and normalize fields in `src/cleaning.py`.
6. Analyze skill frequency in `src/analysis.py`.
7. Visualize and document findings in `notebooks/`.

Expected CSV columns: `job_title`, `company`, `location`, `skills`, `source`, `collected_at`.
