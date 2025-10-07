from fastapi import FastAPI
from .api_client import fetch_crypto_data
from .cleaner import clean_crypto_data
from .db_manager import save_to_db
from dotenv import load_dotenv
from contextlib import asynccontextmanager
import os

load_dotenv()
api_key = os.getenv("COINGECKO_API_KEY")


@asynccontextmanager
async def lifespan(app: FastAPI):
    fetch_and_store()
    yield
    app.state.data = None


app = FastAPI(lifespan=lifespan)


@app.get("/fetch-and-store")
def fetch_and_store():
    raw_data = fetch_crypto_data(api_key)
    cleaned_df = clean_crypto_data(raw_data)
    save_to_db(cleaned_df)
    return {"status": "Data fetched, cleaned, and stored in database"}
