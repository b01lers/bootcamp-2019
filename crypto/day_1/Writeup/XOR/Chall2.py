from binascii import hexlify, unhexlify
#This generates ciphertext
def x0r(s1,s2):
    o = ''
    for i in range(len(s1)):
        o += chr((ord(s1[i]) ^ ord(s2)))    
    return o

#Bruteforce for flag
def brute(c):
    for i in range(128):
        o = x0r(c,chr(i))
        print("Currently testing:  %s" % o)
        if 'b00tcamp' in o:
            print("The key is %c" % chr(i))
            break 

#For uppercase alphabet we have A= '65' and Z = '90' so 26 possibilities for XOR
#I'll use 'X'

#Ciphertext Generation
m = "b00tcamp{brut3f0rc1ng_f1rst_b1ts}"
key = 'X'
c = hexlify(x0r(m,key))
print(brute(unhexlify(c)))

