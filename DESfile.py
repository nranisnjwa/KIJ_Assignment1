import hashlib
from Crypto import Random
from Crypto.Cipher import AES, DES 
from base64 import b64encode, b64decode
import sys



class DESCipher(object):
    def __init__(self, key):
        self.block_size = DES.block_size
        self.key = hashlib.sha256(key.encode()).digest()[:8]

    def encrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        cipher = DES.new(self.key, DES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(encrypted_text).decode("utf-8"), b64encode(cipher.iv).decode("utf-8")

    def decrypt(self, encrypted_text,iv):
        encrypted_text = b64decode(encrypted_text)
        iv =b64decode(iv)
        cipher = DES.new(self.key, DES.MODE_CBC, iv)
        plain_text = cipher.decrypt(encrypted_text)
        return self.__unpad(plain_text)

    def __pad(self, plain_text):
        number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text

    @staticmethod
    def __unpad(plain_text):
        last_character = plain_text[len(plain_text) - 1:]
        return plain_text[:-ord(last_character)]


if __name__ == '__main__':
    key="Attack On Titan!"
    plaintext="Halo Eren Yeager"
    aes=DESCipher(key)
    print("sender",plaintext)
    ciphertext,iv=aes.encrypt(plaintext)
    plaintext=aes.decrypt(ciphertext,iv)
    print("receiver",plaintext)
    print(ciphertext)


