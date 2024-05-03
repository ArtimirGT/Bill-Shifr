from itertools import cycle
def form_dict():
    return dict([(i, chr(i)) for i in range(127)])

def comparator(value, key):
    return dict([(idx, [ch[0], ch[1]])
                for idx, ch in enumerate(zip(value, cycle(key)))])

def encode_val(word):
    d = form_dict()
    return [k for c in word for k,v in d.items() if v == c]

def full_encode(value, key):
    d = comparator(value, key)
    l = len(form_dict())
    return [(v[0] + v[1]) % l for v in d.values()]

def decode_val(list_in):
    l = len(list_in)
    d = form_dict()
    return [d[i] for i in list_in if i in d]

def full_decode(value, key):
    d = comparator(value, key)
    l = len(form_dict())
    return [(v[0] - v[1]) % l for v in d.values()]

word = 'Hello world'
key = 'key'

print(form_dict())
print('Слово: '+ word)
print('Ключ: '+ key)

key_encoded = encode_val(key)
value_encoded = encode_val(word)
 
print('Value= ',value_encoded)
print('Key= ', key_encoded)

shifre = full_encode(value_encoded, key_encoded)
print(shifre)
print('Шифр=', ''.join(decode_val(shifre)))

decoded = full_decode(shifre, key_encoded)
print('Decode list=', decoded)
decode_word_list = decode_val(decoded)
print('Word=',''.join(decode_word_list))