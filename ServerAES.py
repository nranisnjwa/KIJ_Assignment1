
from fileinput import filename
import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes


sock = socket.socket()
sock.bind(('0.0.0.0', 5001))
sock.listen(5)

filename="zoro.png"

while True:
    con, addr = sock.accept()
    print('Connected with ', addr)
    data = con.recv(1024)
    print(data.decode())
    
    key = get_random_bytes(32)
    print(key)

    
    
    cipher = AES.new(key, AES.MODE_CBC) 
    ciphered_data = cipher.encrypt(pad(data, AES.block_size)) 
    file_out = open("encr_"+filename, "wb") 
    file_out.write(cipher.iv)
    file_out.write(ciphered_data) 
    file_out.close()
    
    file = open("encr_"+filename,"rb")
    data = file.read()
   
    while(data):
        con.send(data)
        data = file.read()
    
    print('File has been transferred successfully.')

    con.close()
    break