import requests
from datetime import datetime

def get_eth_price():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
        response = requests.get(url, timeout=5)
        data = response.json()
        return data["ethereum"]["usd"]
    except Exception as e:
        print("Error fetching price:", e)
        return None

price = get_eth_price()

if price:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] Ethereum price: ${price}")