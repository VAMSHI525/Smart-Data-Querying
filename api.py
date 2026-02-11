from fastapi import FastAPI
from pydantic import BaseModel

from schema import TABLE_SCHEMA
from generate_sql import generate_sql
from db_executor import execute_query
from generate_summary import generate_summary

app = FastAPI(title="SQL Generator API")

class SQLRequest(BaseModel):
    user_prompt: str

class SQLResponse(BaseModel):
    user_prompt: str
    generated_sql: str
    summary:str
    result: list

@app.post("/generate-sql", response_model=SQLResponse)
def generate_sql_api(request: SQLRequest):
    sql_query = generate_sql(request.user_prompt, TABLE_SCHEMA)
    print(sql_query)
    result = execute_query(sql_query)

    summary=generate_summary(request.user_prompt,sql_query,result)
    print(summary)
    return {

        "user_prompt": request.user_prompt,
        "generated_sql": sql_query,
        "summary":summary,
        "result": result
        
    }
