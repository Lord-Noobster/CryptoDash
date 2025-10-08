import requests
from dotenv import load_dotenv
import os

load_dotenv()


class CryptoAPIClient:
    def __init__(self):
        self.api_key = os.getenv("COINGECKO_API_KEY")
        self.session = requests.Session()

    # fetches data from the trading site
    def fetch_crypto_data(self):
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": "bitcoin,etherium",
            "vs_currencies": "usd",
        }

        headers = {
            "x_cg_demo_api_key": self.api_key,
        }

        response = self.session.get(url, params=params, headers=headers)
        return response.json()

    def fetch_crypto_market(self):
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "ids": "bitcoin,etherium",
            "vs_currencies": "usd",
            "price_change_percentage": "24h.7d",
        }

        headers = {
            "x_cg_demo_api_key": self.api_key,
        }

        response = self.session.get(url, params=params, headers=headers)
        return response.json()

    def fetch_historical_data(self, coin):
        url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"
        params = {
            "vs_currencies": "usd",
            "days": "180",
        }

        headers = {
            "x_cg_demo_api_key": self.api_key,
        }

        response = self.session.get(url, params=params, headers=headers)
        return response.json()
