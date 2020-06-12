import random
from time import clock, time


class RSA:
    @classmethod
    def gcd(cls, a, b):
        if b == 0:
            return a
        else:
            return cls.gcd(b, a % b)

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
    def eucliden(cls, e, phi):
        x1 = phi
        y1 = phi
        x2 = e
        y2 = 1

        while x2 != 1:
            temp1 = int(x1/x2)
            temp2 = x1 - (temp1 * x2)
            temp3 = y1 - (temp1 * y2)

            x1 = x2
            y1 = y2
            x2 = temp2 if temp2 > 0 else (temp2 % phi)
            y2 = temp3 if temp3 > 0 else temp3 % (phi)

        return y2

    @classmethod
    def generate_e(cls, phi):
        e = random.randint(1, phi)

        if(cls.if_prime(e) == False):
            e = cls.generate_e(phi)

        g = cls.gcd(e, phi)

        if(g != 1):
            e = cls.generate_e(phi)
        return e

    @classmethod
    def generate_key(cls):
        # p = 5062283
        # q = 6515623
        # e = 287
        # d = 11952359793791

        p = random.randint(100, 1000)
        while cls.if_prime(p) != True:
            p = random.randint(100, 1000)
        q = random.randint(100, 1000)
        while cls.if_prime(q) != True:
            q = random.randint(100, 1000)
        n = p * q
        phi = (p - 1) * (q - 1)
        e = cls.generate_e(phi)
        # e = 47
        # d = 103
        d = cls.eucliden(e, phi)
        return ((n, e), (n, d))

    @classmethod
    def encrypt(cls, pk, plainString):
        n, e = pk

        cipherArray = []
        # Start Timer
        start_time = time()
        for i, v in enumerate(plainString):
            # print(v)
            val = pow(ord(v), e, n)
            cipherArray.append(val)
        # End Timer
        end_time = time()
        cipherString = '-'.join((map(str, cipherArray)))
        return (cipherString, round((end_time - start_time) * 1000, 4))

    @classmethod
    def decrypt(cls, pk, cipherFileString):
        # cipherFileArray = list(map(int, cipherFileString.split("-")))
        n, d = pk
        plain_hex_arr = []
        # Start Timer
        start_time = time()
        for i, v in enumerate(cipherFileString):
            val = pow(ord(v), d, n)
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
