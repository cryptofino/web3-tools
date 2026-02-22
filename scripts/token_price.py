import sys
from utils import get_json

def get_token_price(token: str):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={token}&vs_currencies=usd"
    data = get_json(url)

    if token not in data:
        print(f"Token '{token}' not found. Try: bitcoin, ethereum, solana")
        return None

    return data[token]["usd"]

def main():
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print("Usage: python scripts/token_price.py <token_id>")
        print("Example: python scripts/token_price.py ethereum")
        return

    token = sys.argv[1] if len(sys.argv) > 1 else "bitcoin"

    try:
        price = get_token_price(token)
        if price is not None:
            print(f"{token.capitalize()} price: ${price}")
    except Exception as e:
        print("Error fetching token price:", e)

if __name__ == "__main__":
    main()