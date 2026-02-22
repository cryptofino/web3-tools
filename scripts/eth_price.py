from datetime import datetime
from utils import get_json

def get_eth_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    data = get_json(url)
    return data["ethereum"]["usd"]

try:
    price = get_eth_price()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] Ethereum price: ${price}")
except Exception as e:
    print("Error fetching ETH price:", e)