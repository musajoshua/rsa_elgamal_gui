import random
from time import clock, time


class ELGamal:
    @classmethod
    def if_prime(cls, n):
        if (n <= 1):
            return False
        if (n <= 3):
            return True

        if (n % 2 == 0 or n % 3 == 0):
            return False

        i = 5
        while(i * i <= n):
            if (n % i == 0 or n % (i + 2) == 0):
                return False
            i = i + 6

        return True

    @classmethod
    def gcd(cls, a, b):
        if a < b:
            return cls.gcd(b, a)
        elif a % b == 0:
            return b
        else:
            return cls.gcd(b, a % b)

    @classmethod
    def modInverse(cls, a, m):
        a = a % m
        for x in range(1, m):
            if ((a * x) % m == 1):
                return x
        return 1

    @classmethod
    def gen_a(cls, q):
        a = random.randint(100, q)
        while cls.gcd(a, q) != 1:
            a = random.randint(100, q)
        return a

    @classmethod
    def generate_key(cls):
        # p = 76481
        # g = 15442
        # x = 30951
        # y = 26297
        p = random.randint(100, 1000)
        while cls.if_prime(p) != True:
            p = random.randint(100, 1000)
        g = random.randint(100, p - 1)
        x = cls.gen_a(p)
        y = pow(g, x, p)

        return((p, g, y), (p, x))

    @classmethod
    def encrypt(cls, pub_key, plainString):
        p, g, y = pub_key

        k = cls.gen_a(p)

        c1 = pow(g, k, p)
        cipherArray = []
        # Start Timer
        start_time = time()
        for i, v in enumerate(plainString):
            val = (pow(y, k) * v) % p
            cipherArray.append(val)
        # End Timer
        end_time = time()
        cipherString = '-'.join((map(str, cipherArray)))
        return ((c1, cipherString), round((end_time - start_time) * 1000, 4))

    @classmethod
    def decrypt(cls, pri_key, c1, cipherFileString):
        cipherFileArray = list(map(int, cipherFileString.split("-")))
        p, x = pri_key
        c1 = int(c1)
        plain_hex_arr = []
        # Start Timer
        start_time = time()
        for i, v in enumerate(cipherFileArray):
            k = cls.modInverse(pow(c1, x), p)
            val = (k * v) % p
            plain_hex_arr.append(val)
        end_time = time()
        # End Timer
        plain_hex_string = cls.unifyString(plain_hex_arr)
        return (plain_hex_string, round((end_time - start_time) * 1000, 4))

    @classmethod
    def unifyString(cls, fileArray):
        string = ''
        for i, v in enumerate(fileArray):
            string = string + chr(v)
        return string
