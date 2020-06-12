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
        a = random.randint(1, q-1)
        while cls.gcd(a, q) != 1:
            a = random.randint(1, q-1)
        return a

    @classmethod
    def generate_key(cls):
        # p = random.randint(50, 300)
        # while cls.if_prime(p) != True:
        #     p = random.randint(50, 300)
        # p = 103
        # g = 97
        # x = cls.gen_a(p)
        # y = pow(g, x, p)
        p = 20
        g = 17
        x = cls.gen_a(p)
        print("x is ", x)
        y = pow(g, x, p)
        # p = random.randint(50, 300)
        # g = random.randint(50, p - 1)
        # x = cls.gen_a(p)
        # y = pow(g, x, p)

        return((p, g, y), (p, x))

    @classmethod
    def encrypt(cls, pub_key, plainString):
        p, g, y = pub_key

        c1 = []
        c2 = []
        # Start Timer
        start_time = time()
        k = cls.gen_a(p)
        for i, v in enumerate(plainString):
            c1.append(pow(g, k, p))
            val = (pow(y, k) * v) % p
            c2.append(val)
        # End Timer
        end_time = time()
        cipherString1 = '-'.join((map(str, c1)))
        cipherString2 = '-'.join((map(str, c2)))
        return ((cipherString1, cipherString2), round((end_time - start_time) * 1000, 4))

    @classmethod
    def decrypt(cls, pri_key, cipherFileString1, cipherFileString2):
        cipherFileArray1 = list(map(int, cipherFileString1.split("-")))
        cipherFileArray2 = list(map(int, cipherFileString2.split("-")))
        p, x = pri_key
        plain_hex_arr = []
        # Start Timer
        start_time = time()
        for i, v in enumerate(cipherFileArray2):

            k = pow(pow(cipherFileArray1[i], x), p-2, p)

            # k = pow(cipherFileArray1[i], (p - 1 - x))

            # k = pow(pow(c1, x), (p - 2) * v) % p
            # k = cls.modInverse(pow(c1, x), p)
            val = (k * v) % p
            # val = pow(pow(c1, x), (p - 2) * v, p)
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
