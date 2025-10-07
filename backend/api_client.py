import requests


# fetches data from the trading site
def fetch_crypto_data(api_key):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,etherium",
        "vs_currencies": "usd",
        "x_cg_demo_api_key": api_key,
    }

    response = requests.get(url, params=params)
    return response.json()
