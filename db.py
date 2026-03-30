def execute_query(query: str):
    # fake data (temporary)
    students = [
        ["Aman"],
        ["Ravi"],
        ["Neha"],
        ["Priya"]
    ]

    if "select" in query.lower():
        return students

    return []