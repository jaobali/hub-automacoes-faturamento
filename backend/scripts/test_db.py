import psycopg

conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="hub",
    user="postgres",
    password="postgres",
)

with conn.cursor() as cur:
    cur.execute("SELECT version();")

    result = cur.fetchone()

    print(result)

conn.close()