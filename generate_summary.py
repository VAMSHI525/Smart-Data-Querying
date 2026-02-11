from huggingface_hub import InferenceClient

HF_API_TOKEN = "<Huggingface_Read_Token>"
MODEL_NAME = "openai/gpt-oss-120b" #"meta-llama/Meta-Llama-3-8B-Instruct" #"meta-llama/Meta-Llama-3-8B-Instruct"


def generate_summary(user_prompt: str,generated_sql,result ):
    client = InferenceClient(
        model=MODEL_NAME,
        token=HF_API_TOKEN
    )
    
    response = client.chat_completion(
        messages=[
            {
                "role": "system",
                "content":f"""You are a data analyst assistant

                    Your task is to generate a clear, concise, and business-friendly summary
                    based on:
                    - a user's natural language question
                    - the SQL query generated to answer it
                    - the query result data

                    Rules:
                    - Do NOT mention SQL syntax unless useful
                    - Do NOT explain how the query works
                    - Focus on insights derived from the result
                    - If the result is empty, clearly state that no data was found
                    - Use simple, professional language
                    - Keep the summary short"""

            },
            {
                "role": "user",
                "content": f"""User Question:
                        {user_prompt}

                        Generated SQL Query:
                        {generated_sql}

                        Query Result:
                        {result}

                        Generate a human-readable summary of the result.
                        """
            }
        ],
        max_tokens=300,
        temperature=0.1
    )
    
    return response.choices[0].message.content



# if __name__ == "__main__":
#     question = input("Ask your question: ")
#     sql = generate_sql(question)
#     print("\nGenerated SQL:\n")
#     print(sql)

