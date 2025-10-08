import pandas as pd
from backend.lists import numeric_cols


class DataCleaner:
    def clean_crypto_data(self, raw_data):
        df = pd.DataFrame(raw_data).T.reset_index()
        df.columns = ["coin", "price_usd"]
        df["price_usd"] = pd.to_numeric(df["price_usd"], errors="coerce")
        return df.dropna()

    def clean_crypto_market_data(self, raw_data):
        df = pd.json_normalize(raw_data)
        df.columns = [
            "name",
            "symbol",
            "current_price",
            "market_cap",
            "total_volume",
            "price_change_percentage_24h",
            "price_change_percentage_7d",
            "circulating_supply",
            "total_supply",
        ]
        df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, erros="coerce")

    def clean_historical_data(self, raw_data):
        df_prices = pd.DataFrame(raw_data["prices"], columns=["timestamp", "price"])
        df_market_caps = pd.DataFrame(
            raw_data["market_caps"], columns=["timestamp", "market_cap"]
        )
        df_volumes = pd.DataFrame(
            raw_data["total_volumes"], columns=["timestamp", "total_volume"]
        )

        df = df_prices.merge(df_market_caps).merge(df_volumes)
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        return df
