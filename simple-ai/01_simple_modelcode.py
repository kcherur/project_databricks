from openai import OpenAI
import os

# How to get your Databricks token: https://docs.databricks.com/en/dev-tools/auth/pat.html
DATABRICKS_TOKEN = 'testtesttest'
# Alternatively in a Databricks notebook you can use this:
# DATABRICKS_TOKEN = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()

client = OpenAI(
    api_key=DATABRICKS_TOKEN,
    base_url="https://7474647958441679.ai-gateway.cloud.databricks.com/mlflow/v1"
)

response = client.chat.completions.create(
    model="databricks-meta-llama-3-1-8b-instruct",
    messages=[
        {
            "role": "user",
            "content": "Who was the first president of India? Provide 1 sentence answer only"
        }
    ],
    max_tokens=5000
)

print(response.choices[0].message.content)