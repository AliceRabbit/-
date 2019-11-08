from Crypto.Util.number import getPrime


def int_to_bytes(n):
    """把int转化成byte"""
    return n.to_bytes((n.bit_length() + 7) // 8, 'big')


def gcd(a, b):
    """求最大公约数"""
    while b != 0:
        a, b = b, a % b

    return a


def lcm(a, b):
    """求最小公倍数"""
    return a // gcd(a, b) * b


def mod_inv(a, n):
    """求模n时的乘法逆"""
    t, r = 0, n
    new_t, new_r = 1, a

    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r

    if r > 1:
        raise Exception("a is not invertible")
    if t < 0:
        t = t + n

    return t


class RSA:
    """RSA加解密实现"""

    def __init__(self, key_length):
        """e固定为3，寻找合适的p和q"""
        self.e = 3
        phi = 0

        while gcd(self.e, phi) != 1:
            p, q = getPrime(key_length // 2), getPrime(key_length // 2)
            phi = lcm(p - 1, q - 1)
            self.n = p * q

        self._d = mod_inv(self.e, phi)

    def encrypt(self, binary_data):
        """将传入的文本转化为int型进行加密"""
        int_data = int.from_bytes(binary_data, byteorder='big')
        return pow(int_data, self.e, self.n)

    def decrypt(self, encrypted_int_data):
        """(int -> bytes)"""
        int_data = pow(encrypted_int_data, self._d, self.n)
        return int_to_bytes(int_data)


def main():

    # 测试求逆元
    assert mod_inv(17, 3120) == 2753

    # 测试RSA算法
    rsa = RSA(1024)
    some_text = b"Hello, let's try if the RSA code works"
    assert rsa.decrypt(rsa.encrypt(some_text)) == some_text


if __name__ == '__main__':
    main()