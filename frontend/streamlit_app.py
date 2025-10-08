import streamlit as st
import pandas as pd
import sqlite3
from pathlib import Path
from backend.lists import coins_list

db_path = Path(__file__).parent.parent / "data" / "crypto.db"

conn = sqlite3.connect(db_path)
df = pd.read_sql_query("SELECT * FROM Market-Overview", conn)
conn.close()
selected_coin = st.selectbox("choose a coin", coins_list)
# selected_coin should then be passed to the sql db to fetch that coins data from the db
# add functionality that if no data is in the db or the data is older than x time it fetches it
# should probably be done in the back end as it currently is fetching all data on load so on load it checks -
# if the data is in the db or if the data is too old and then fetch new data if its too old or non existent
