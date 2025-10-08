from fastapi import FastAPI
from .api_client import CryptoAPIClient
from .cleaner import DataCleaner
from .db_manager import save_to_db
from .lists import coins_list
from contextlib import asynccontextmanager

client = CryptoAPIClient()
cleaner = DataCleaner()


def fetch_historic_loop():
    for coin in coins_list:
        raw_data = client.fetch_historical_data(coin)
        cleaned_df = cleaner.clean_historical_data(raw_data)
        table_name = f"{coin}_historic"
        save_to_db(cleaned_df, table_name)


def fetch_market_overview():
    raw_data = client.fetch_crypto_market()
    cleaned_df = cleaner.clean_crypto_market_data(raw_data)
    table_name = "Market-Overview"
    save_to_db(cleaned_df, table_name)


def fetch_and_store_data():  # need refactoring on run it should pull top 5 coins historical and market info
    fetch_historic_loop()  # loops through coins_list from lists.py fetching historical data for 5 coins


@asynccontextmanager
async def startup_shutdown(app: FastAPI):
    fetch_and_store_data()
    yield
    app.state.data = None


app = FastAPI(lifespan=startup_shutdown)


@app.get("/trigger-data-fetch")
def trigger_data_fetch():
    fetch_and_store_data()
    return {"status": "Data fetched, cleaned, and stored in database"}
