from scripts.utils import get_json

def get_gas_prices():
    url = "https://api.etherscan.io/api?module=gastracker&action=gasoracle"
    data = get_json(url)
    return data["result"]

def main():
    try:
        gas = get_gas_prices()
        print("Safe Gas Price:", gas["SafeGasPrice"])
        print("Propose Gas Price:", gas["ProposeGasPrice"])
        print("Fast Gas Price:", gas["FastGasPrice"])
    except Exception as e:
        print("Error fetching gas prices:", e)

if __name__ == "__main__":
    main()