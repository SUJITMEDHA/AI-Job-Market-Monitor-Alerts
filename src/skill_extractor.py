SKILL_KEYWORDS = [
    "python", "sql", "spark", "airflow", "aws", "gcp",
    "pytorch", "tensorflow", "llm", "nlp",
    "dbt", "snowflake", "ml", "data engineering"
]

def extract_skills(text: str):
    text = text.lower()
    return [skill for skill in SKILL_KEYWORDS if skill in text]
