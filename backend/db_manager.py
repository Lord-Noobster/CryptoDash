import sqlite3
from pathlib import Path


def save_to_db(
    df, table_name, db_path=Path(__file__).parent.parent / "data" / "crypto.db"
):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
