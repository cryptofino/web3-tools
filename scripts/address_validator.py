def is_valid_eth_address(address):
    return address.startswith("0x") and len(address) == 42

test_address = "0x0000000000000000000000000000000000000000"

if is_valid_eth_address(test_address):
    print("Valid Ethereum address format")
else:
    print("Invalid Ethereum address format")