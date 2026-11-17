"""Cleaning helpers for job listing data."""
import pandas as pd

def clean_jobs(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.strip().lower() for c in df.columns]
    for col in ("job_title", "company", "location", "skills"):
        if col in df.columns:
            df[col] = df[col].astype("string").str.strip()
    return df.drop_duplicates()
