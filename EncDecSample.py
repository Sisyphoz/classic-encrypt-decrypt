# Functional version of simple encrypt/decrypt algorithms.

from secrets import token_bytes
from typing import Tuple

def rand_key(length: int) -> int:

    tb: bytes = token_bytes(length)
    return int.from_bytes(tb, "big")

def encrypt(original: str) -> Tuple[int, int]:

    original_bytes: bytes = original.encode()
    dummy: int = rand_key(len(original_bytes))

    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy
    return dummy, encrypted

def decrypt(key1: int, key2: int) -> str:

    decrypted: int = key1 ^ key2
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()

message = "go ahead and try again @ 17:00 at the same place"
key1, key2 = encrypt(message)
result: str = decrypt(key1, key2)

print('Random key:',rand_key(3))
print(f'Encrypted message "{message}" using previous random key:')
print(encrypt(message))
print('Lets decrypt previous message:')
print(result)
