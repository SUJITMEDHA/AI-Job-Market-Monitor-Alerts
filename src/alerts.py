def should_alert(skills):
    """
    Trigger alert if hot skills appear
    """
    hot_skills = {"llm", "pytorch", "spark", "airflow"}
    return any(skill in hot_skills for skill in skills)
