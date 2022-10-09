from telnetlib import ENCRYPT
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA
from Crypto.Random import get_random_bytes



def encrypt(key,plaintext):
		return ARC4.new(key).encrypt(plaintext)

def decrypt(key,msg):
		return ARC4.new(key).decrypt(msg)


key = b'Attack On Titan!'
plaintext =b'Halo Eren Yeager'
nonce = get_random_bytes(16)
tempkey = SHA.new(key+nonce).digest()
cipher = ARC4.new(tempkey)
msg = nonce + cipher.encrypt(plaintext)


print(plaintext)
print(msg)
