import binascii

def encodeRepeatingKeyXor(s, key):
    return bytes([s[i] ^ key[i % len(key)] for i in range(len(s))])

x = b'''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
key = b'ICE'

if __name__ == '__main__':
    y = encodeRepeatingKeyXor(x, key)
    encodedY = binascii.hexlify(y).decode('ascii')
    print(encodedY)