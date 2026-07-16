import psycopg
import os
from dotenv import load_dotenv
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(ROOT_DIR / ".env")

print(os.getenv("POSTGRES_PASSWORD"))

conn = psycopg.connect(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
)

with conn.cursor() as cur:
    cur.execute("SELECT version();")
    result = cur.fetchone()
    print(result)

conn.close()