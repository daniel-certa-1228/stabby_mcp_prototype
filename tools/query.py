import psycopg2.extras
from db import get_connection
import json


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


def get_knife_list():
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                """
                SELECT * 
                FROM view_knife_grid
                ORDER BY brand, knife;
                """
            )
            rows = cur.fetchall()
            return json.dumps([dict(row) for row in rows], indent=2, default=str)
    finally:
        conn.close()
