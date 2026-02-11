import pyodbc
from config import SQL_SERVER_CONN_STR

#     return columns, rows

def execute_query(sql: str):
    conn = pyodbc.connect(SQL_SERVER_CONN_STR)
    cursor = conn.cursor()

    if not sql or not sql.strip():
        raise ValueError("Generated SQL is empty")
    
    cursor.execute(sql)

    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()

    results = [dict(zip(columns, row)) for row in rows]

    cursor.close()
    conn.close()

    return results
