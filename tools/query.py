import psycopg2.extras
from db import get_connection


def list_tables():
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                """
                SELECT table_name 
                FROM information_schema.tables
                WHERE table_schema = 'public'
                ORDER BY table_name;
            """
            )
            rows = cur.fetchall()
            return [row["table_name"] for row in rows]
    finally:
        conn.close()
