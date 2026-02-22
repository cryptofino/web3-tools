import requests
import sys

def get_token_price(token):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={token}&vs_currencies=usd"
        response = requests.get(url, timeout=5)
        data = response.json()
        return data[token]["usd"]
    except Exception as e:
        print("Error fetching price:", e)
        return None

if len(sys.argv) > 1:
    token = sys.argv[1]
else:
    token = "bitcoin"

price = get_token_price(token)

if price:
    print(f"{token.capitalize()} price: ${price}")