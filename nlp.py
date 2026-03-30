def generate_sql(question: str) -> str:
    q = question.lower()

    if "how many" in q or "count" in q:
        return "SELECT COUNT(*) FROM students"

    if "list" in q or "show" in q:
        return "SELECT name FROM students"

    # 👉 NEW code niche add karo
    if "all data" in q:
        return "SELECT * FROM students"

    if "show names" in q:
        return "SELECT name FROM students"

    # default
    return "SELECT name FROM students"