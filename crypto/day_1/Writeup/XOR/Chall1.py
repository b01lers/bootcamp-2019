from binascii import unhexlify, hexlify
#This generates ciphertext
def x0r(s1,s2):
    o = ''
    for i in range(len(s1)):
        o += chr((ord(s1[i]) ^ ord(s2)))    
    return o
m = "b00tcamp{n0nrand0m_0n3_t1m3_p4d}"
key = 'A'
#print("Ciphertext: ")
#print(x0r(m, key))
c = hexlify(x0r(m,key))
#This retrieves original message
print("Original Message: ")
print(x0r(unhexlify(c),key)) 
