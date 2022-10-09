#RC4 Encryption XOR 
    
location = r'C:\Users\USER\work\Usopp.jpg'
key = int(input('Enter Key to encrypt Image: '))
     
print('The location file is: ', location)
print('Key for Encryption Image is: ', key)

fin = open(location, 'rb')
     
image = fin.read()
fin.close()
     
image = bytearray(image)
 
for index, values in enumerate(image):
	image[index] = values ^ key
 
fin = open(location, 'wb')

fin.write(image)
fin.close()
print('Done Encrypted Image File!')
 
    
