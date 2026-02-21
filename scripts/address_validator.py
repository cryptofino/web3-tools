import re

def is_valid_eth_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    if not address.startswith("0x"):
        return False
    if len(address) != 42:
        return False
    return re.fullmatch(r"0x[a-fA-F0-9]{40}", address) is not None

tests = [
    "0x0000000000000000000000000000000000000000",
    "0xZZ00000000000000000000000000000000000000",
    "0x123",
    "123",
]

for t in tests:
    print(t, "=>", is_valid_eth_address(t))