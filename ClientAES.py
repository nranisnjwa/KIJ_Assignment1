import socket
from Crypto.Cipher import AES 
from Crypto.Util.Padding import unpad

sock = socket.socket()

port = 5001
host ='localhost'

sock.connect((host,port))
print('Connected to server')
sock.send('Client is connected'.encode())

data = sock.recv(99999)

filename = "zoro.png"


while(data):
    
   
    file_in = open(filename, 'rb') 
    iv = file_in.read(16) 
    ciphered_data = file_in.read()

    cipher = AES.new(key, AES.MODE_CBC, iv=iv) 
    original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size) 
    
    
    file_out = open("decr_"+filename, "wb") 
    file_out.write(original_data)
    
    data = sock.recv(99999)

print('File has been received successfully.')

file_out.close()
file_in.close()
sock.close()
print('Connection Closed.')


