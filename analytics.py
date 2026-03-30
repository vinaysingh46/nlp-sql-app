queries = []
times = []

def track_query(q, t):
    queries.append(q)
    times.append(t)

def get_stats():
    return {
        "total_queries": len(queries),
        "slowest_query_time": max(times) if times else 0
    }