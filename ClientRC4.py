import socket
import tqdm
import os
import RC4

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

host = "192.168.1.101"
port = 5001
location = r'C:\Users\USER\work\Usop.png'
filesize = os.path.getsize(location)

s = socket.socket()

print(f"[+] Connecting to {host} : {port}")
s.connect ((host, port))
print("[+] Connected.")

s.send(f"{location}{SEPARATOR}{filesize}".encode())

progress = tqdm.tqdm(range(filesize), f"Sending {location}", unit-"B", unit_scale=True, unit_divisor=1024)
with open(location, "rb") as f:

    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        s.sendall(bytes_read)
        progress.update(len(bytes_read))

s.close()