import binascii
from Crypto.Util.strxor import strxor

encodedS = '1c0111001f010100061a024b53535009181c'
encodedT = '686974207468652062756c6c277320657965'

s = binascii.unhexlify(encodedS)
t = binascii.unhexlify(encodedT)

u = strxor(s, t)
print(u)