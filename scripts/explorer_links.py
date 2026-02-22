def get_etherscan_address_link(address: str) -> str:
    return f"https://etherscan.io/address/{address}"

def get_etherscan_tx_link(tx_hash: str) -> str:
    return f"https://etherscan.io/tx/{tx_hash}"

if __name__ == "__main__":
    sample_address = "0x0000000000000000000000000000000000000000"
    sample_tx = "0x1234567890abcdef"
    print("Address link:", get_etherscan_address_link(sample_address))
    print("Transaction link:", get_etherscan_tx_link(sample_tx))