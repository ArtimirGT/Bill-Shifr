from binascii import *
'''def binary_to_text(n):
    for x in n:
        s = ''.join(chr(int(n[i*8:i*8+8],2)) for i in range(len(n)//8))
    return s

def text_to_bindary(n):
    s = ''.join(format(ord(x), 'b') for x in n)
    return s'''

def encode(n):
    return ''.join([format(ord(i), '08b') for i in n])

def decode(n):
    return ''.join(chr(int(n[i:i+8], 2)) for i in range(0, len(n), 8))

st = 'aboba'

s = encode(st)

print(s)
print(decode(s))