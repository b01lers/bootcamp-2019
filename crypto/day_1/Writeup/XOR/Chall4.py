from binascii import hexlify, unhexlify

#XOR function
def x0r(s1,s2):
    o = ''
    for i in range(len(s1)):
        o += chr((ord(s1[i % len(s1)]) ^ ord(s2[i % len(s2)])))    
    return o


key = 'y33tG4ng'
m = 'b00tcamp{2^8=256}'

#Hexlify for provided a string that is legible
c = hexlify(x0r(m,key))
key = unhexlify(c)

#Brute key of length 8bytes = 8char = 2^8 = 256 combinations
#With known knowledge that the key is 8bytes consisting of chars (1:1) and the format is b00tcamp{XXXXXX}
def solve(ctext):
    print(ctext)
    o = '\x01\x01\x01\x01\x01\x01\x01\x01' #Test string for all ascii values
    partialM = 'b00tcamp'
    a = ''
    ugh = list(o)

    for i in range(8): #key length
        for j in range(256): #ascii values
            print("Testing character %d" % (i+1))
            ugh[i] = chr(j)
            print(x0r(a.join(ugh),ctext))
            if(x0r(a.join(ugh),ctext)[i] == partialM[i]):
                print("The key is %s" % a.join(ugh))
                key = a.join(ugh)
                break
    #Now using found key
    message = x0r(ctext, key)
    print(message)
print("\n\n\n\n")
print("The cipher is: %s" % c)
print(solve(unhexlify(c)))
