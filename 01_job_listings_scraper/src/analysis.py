"""Basic skill-frequency analysis."""
import pandas as pd

def skill_frequencies(df: pd.DataFrame) -> pd.Series:
    if "skills" not in df.columns:
        raise ValueError("Expected a 'skills' column.")
    skills = (
        df["skills"].dropna().astype(str)
        .str.lower().str.split(r"[,;|]")
        .explode().str.strip()
    )
    skills = skills[skills.ne("")]
    return skills.value_counts()
