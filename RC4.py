#RC4 Encryption XOR 
    
filename = r'C:\Users\USER\work\Usopp.jpg'
key = int(input('Enter Key to encrypt Image: '))
     
print('The location file is: ', filename)
print('Key for Encryption is: ', key)

fin = open(filename, 'rb')
     
image = fin.read()
fin.close()
     
image = bytearray(image)
 
for index, values in enumerate(image):
	image[index] = values ^ key
 
fin = open(filename, 'wb')

fin.write(image)
fin.close()
print('Done Encrypted Image File!')
 
    