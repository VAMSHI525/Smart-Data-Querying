FORBIDDEN_KEYWORDS = [
    "insert", "update", "delete", "drop",
    "alter", "truncate", "merge"
]

def is_safe_sql(sql: str) -> bool:
    sql_lower = sql.lower()
    return (
        sql_lower.startswith("select")
        and not any(keyword in sql_lower for keyword in FORBIDDEN_KEYWORDS)
    )
