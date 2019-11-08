# -*- coding: UTF-8 -*-
import sys
import util
from base64 import b64decode
from pkcs_7_padding import pkcs_padding

def cbc_encrypt(text, key, iv):
    ''' CBC encrypt text with initialization vector iv and key '''
    block_length = len(iv)
    text = pkcs_padding(text, block_length)
    blocks = util.blocks(text, block_length)#分块

    blocks[0] = util.string_xor(blocks[0], iv)#第一块使用预设的iv加密
    blocks[0] = util.ecb_encrypt(blocks[0], key)

    for i in xrange(1, len(blocks)):
        blocks[i] = util.string_xor(blocks[i], blocks[i-1])
        blocks[i] = util.ecb_encrypt(blocks[i], key)

    return ''.join(blocks)

def cbc_decrypt(text, key, iv):
    ''' CBC decrypt text with initialization vector iv and key '''
    block_length = len(iv)
    blocks = util.blocks(text, block_length)

    decoded_blocks = [0] * len(blocks)

    decoded_blocks[0] = util.ecb_decrypt(blocks[0], key)
    decoded_blocks[0] = util.string_xor(decoded_blocks[0], iv)
    for i in xrange(1, len(blocks)):
        decoded_blocks[i] = util.ecb_decrypt(blocks[i], key)
        decoded_blocks[i] = util.string_xor(decoded_blocks[i], blocks[i-1])

    return ''.join(decoded_blocks)


if __name__ == '__main__':
    key = 'YELLOW SUBMARINE'
    iv = '\x00'*16

    # See if sys.argv has iv and key given
    if len(sys.argv) > 2:
        key = sys.argv[1]
        if len(key) != 16:
            print 'Length of key is %d, but should be 16' % (len(key))
            sys.exit(0)

        iv = sys.argv[2]
        if len(iv) != 16:
            print 'Length of IV is %d, but should be 16' % (len(iv))
            sys.exit(0)
    # else:
    #     print '(Optional) Usage: %s key iv\n' % (sys.argv[0])

    # AES CBC encrypt
    text = open('input').read()
    print '''CBC encrypting file 'input' with %s as key, and <%s> as iv (written to cbc_output)''' % (key, repr(iv))
    encrypted_text = cbc_encrypt(text, key, iv)

    with open('cbc_output', 'w') as f:
        f.write(encrypted_text)

    # AES CBC decrypt
    text = open('10.txt').read()
    text = b64decode(text)
    print '''CBC decrypting 10.txt with %s as key, and <%s> as iv (on stdout)''' % (key, repr(iv))
    print cbc_decrypt(text, key, iv)
