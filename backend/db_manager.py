import sqlite3
from pathlib import Path


def save_to_db(df, db_path=Path(__file__).parent.parent / "data" / "crypto.db"):
    conn = sqlite3.connect(db_path)
    df.to_sql("prices", conn, if_exists="replace", index=False)
    conn.close()
