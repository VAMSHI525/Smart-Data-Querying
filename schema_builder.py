# dynamically fetching the schema 
import pyodbc
from collections import defaultdict
from config import SQL_SERVER_CONN_STR

METADATA_QUERY = """
SELECT
    t.name AS table_name,
    c.name AS column_name,
    ty.name AS data_type
FROM sys.tables t
JOIN sys.schemas s
    ON t.schema_id = s.schema_id
JOIN sys.columns c
    ON t.object_id = c.object_id
JOIN sys.types ty
    ON c.user_type_id = ty.user_type_id
WHERE s.name = 'dbo'
ORDER BY t.name, c.column_id;
"""

def build_table_schema() -> str:
    conn = pyodbc.connect(SQL_SERVER_CONN_STR)
    cursor = conn.cursor()
    cursor.execute(METADATA_QUERY)

    schema_map = defaultdict(list)

    for table_name, column_name, data_type in cursor.fetchall():
        schema_map[table_name].append((column_name, data_type))

    cursor.close()
    conn.close()

    schema_text = ""

    for table_name, columns in schema_map.items():
        schema_text += f"Table: {table_name}\n"
        schema_text += "Columns:\n"
        for column_name, data_type in columns:
            schema_text += f"- {column_name} ({data_type})\n"
        schema_text += "\n"

    return schema_text.strip()
