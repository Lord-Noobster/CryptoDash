import pandas as pd


def clean_crypto_data(raw_data):
    df = pd.DataFrame(raw_data).T.reset_index()
    df.columns = ["coin", "price_usd"]
    df["price_usd"] = pd.to_numeric(df["price_usd"], errors="coerce")
    return df.dropna()
