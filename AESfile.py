import os
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES, DES


def getkey(keysize):

       key = os.urandom(keysize)
       return key

def getIV(blocksize):

    iv = os.urandom(blocksize)
    return iv


def encrypt_image(filename, key, iv):

    
    encrypted_filename = "encr_" + filename

    with open(filename, "rb") as file1:
        data = file1.read()

        cipher = AES.new(key, AES.MODE_CBC,iv)
        
    ciphertext = cipher.encrypt(pad(data,BLOCKSIZE))

    with open(encrypted_filename, "wb") as file2:

        file2.write(ciphertext)

    return encrypted_filename 

def decrypted_image(filename, key, iv):

    
    decrypted_filename = "decr_" + filename

    with open(filename, "rb") as file1:
        data = file1.read()

        cipher2 = AES.new(key, AES.MODE_CBC, iv)

        decrypted_data = unpad(cipher2.decrypt(data),BLOCKSIZE)

    with open(decrypted_filename, "wb") as file2:

        file2.write(decrypted_data)

    return decrypted_filename

KEYSIZE = 16
BLOCKSIZE = 16
filename = "zoro.png"

key = getkey(KEYSIZE)
iv = getIV(BLOCKSIZE)

encrypted_filename = encrypt_image(filename, key, iv)
decrypted_filename = decrypted_image(encrypted_filename, key, iv)



