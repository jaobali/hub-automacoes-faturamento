from fastapi import APIRouter
from database.connection import get_connection

router = APIRouter()

@router.get("/status")
def status():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1;")
            result = cur.fetchone()

    return {
        "status": "ok",
        "database": {
            "connected": True,
            "query_result": result[0],
        },
    }