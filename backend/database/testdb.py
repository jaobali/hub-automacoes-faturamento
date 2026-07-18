import psycopg
from core.settings import settings

conn = psycopg.connect(
    host=settings.POSTGRES_HOST,
    port=settings.POSTGRES_PORT,
    dbname=settings.POSTGRES_DB,
    user=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
)

with conn.cursor() as cur:
    cur.execute("SELECT 1 + 1 as sum;")
    result = cur.fetchone()
    print(result)

conn.close()