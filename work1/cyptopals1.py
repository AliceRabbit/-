import binascii
import base64

def hexToBase64(s):
    decoded = binascii.unhexlify(s)
    return base64.b64encode(decoded).decode('ascii')

x = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
y = hexToBase64(x)
print(y)