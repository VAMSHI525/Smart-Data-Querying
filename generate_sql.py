from huggingface_hub import InferenceClient

HF_API_TOKEN = "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"
MODEL_NAME = "openai/gpt-oss-120b" #"meta-llama/Meta-Llama-3-8B-Instruct" #"meta-llama/Meta-Llama-3-8B-Instruct"


def generate_sql(user_prompt: str, schema):
    # print (schema)
    client = InferenceClient(
        model=MODEL_NAME,
        token=HF_API_TOKEN
    )
    
    response = client.chat_completion(
        messages=[
            {
                "role": "system",
                "content": f"""
You are an expert SQL query generator for MS SQL Server with deep knowledge of database design and optimization.

Rules:
- Generate SQL only do not add extra special characters, it should be database ready executed query.
- No markdown, no comments
- Generate SQL queries only for MS SQL Server
- Should give only one optimal query for a question
- Use the schema exactly as provided
- Do not explain the query
- Use standard SQL (ANSI style)
- SELECT queries only
- OUTPUT ONLY valid SQL

Schema:
{schema}
"""
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        max_tokens=500,
        temperature=0.1
    )

    sql_query = response.choices[0].message.content.strip()
    print(sql_query)
    return sql_query


# if __name__ == "__main__":
#     question = input("Ask your question: ")
#     sql = generate_sql(question)
#     print("\nGenerated SQL:\n")
#     print(sql)
