from scraper import fetch_jobs
from skill_extractor import extract_skills
from alerts import should_alert

def run():
    print("🚀 AI JOB MARKET MONITOR STARTED\n")

    jobs = fetch_jobs()
    print(f"📊 Jobs fetched: {len(jobs)}\n")

    for job in jobs:
        skills = extract_skills(job["description"])
        alert = should_alert(skills)

        print(f"🧑‍💼 Role: {job['title']}")
        print(f"🏢 Company: {job['company']}")
        print(f"📍 Location: {job['location']}")
        print(f"🧠 Skills: {skills}")

        if alert:
            print("🔥 ALERT: High-demand AI/Data skills detected!")

        print("-" * 50)

if __name__ == "__main__":
    run()
