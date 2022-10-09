

def keys(key):
    S = [x for x in range(0, 256)]
    j=0
    key=[ord(x) for x in key]

    for i in range(256): 
        j=(j+S[i]+int(key[i%len(key)]))%256
    return S

def encryptor(S, plaintext):
    i,j=0, 0 
    ciphertext=[]
    for char in plaintext:
        i=(i+j)%256
        j=(j+S[i])%256
        S[i], S[j]=S[j], S[i]
        hexed = format(ord(chr(S[(S[i]+S[j])%256] ^ ord(char))), 'x')
        ciphertext.append(hexed)

        return ciphertext




key = input("\nEnter your key: ")
S = keys(key)
ciphertext = encryptor(S, input('\nEnter plaintext: '))

print("\nYour Ciphertext is: ")
for x in ciphertext:
    print (x, end='')
print("\n")


