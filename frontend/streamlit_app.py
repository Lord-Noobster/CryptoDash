import streamlit as st
import pandas as pd
import sqlite3
from pathlib import Path

db_path = Path(__file__).parent.parent / "data" / "crypto.db"

conn = sqlite3.connect(db_path)
df = pd.read_sql("SELECT * FROM prices", conn)
st.write(df)
st.line_chart(df.set_index("coin"))
