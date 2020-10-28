# -----------------------------------------------------------
# RSA Class that Performs the Generation, Encryption and Decryption of a string
#
# (C) 2020 Musa Joshua Gideon-Bashir, Abuja, Nigeria
# Released under MIT Public License
# email gidijosh@gmail.com
# -----------------------------------------------------------


import random
from time import clock, time
from .encoding import encode, decode


class RSA:
    """
    RSA Class that Performs the Generation, Encryption and Decryption of a string
    """
    @classmethod
    def gcd(cls, a, b):
        """finds the gcd of two numbers a and b

        Args:
            cls (class attribute): Access a class atribute through keyword cls
            a: integer a 
            b: integer b 

        Returns:
            int: gcd of the two numbers
        """
        if b == 0:
            return a
        else:
            return cls.gcd(b, a % b)

    @classmethod
    def if_prime(cls, n):
        """Checks if a number is a prime or not

        Args:
            cls (class attribute): Access a class atribute through keyword cls

        Returns:
            boolean: true or false
        """
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
        """finds d, using the extended euclidean algorithm

        Args:
            cls (class attribute): Access a class atribute through keyword cls
            e: integer e
            phi: integer phi

        Returns:
            int: d
        """
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
        """finds e such that 0 < e < phi and the GCD of e and phi is 1.

        Args:
            cls (class attribute): Access a class atribute through keyword cls
            phi: integer phi

        Returns:
            int: e
        """
        e = random.randint(1, phi)

        if(cls.if_prime(e) == False):
            e = cls.generate_e(phi)

        g = cls.gcd(e, phi)

        if(g != 1):
            e = cls.generate_e(phi)
        return e

    @classmethod
    def generate_keys(cls):
        """generates the keys

        Args:
            cls (class attribute): Access a class atribute through keyword cls

        Returns:
            int: n
            int: e
            int: d
        """
        p = random.randint(100, 1000)
        while cls.if_prime(p) != True:
            p = random.randint(100, 1000)
        q = random.randint(100, 1000)
        while cls.if_prime(q) != True:
            q = random.randint(100, 1000)
        n = p * q
        phi = (p - 1) * (q - 1)
        e = cls.generate_e(phi)
        d = cls.eucliden(e, phi)
        return ((n, e), (n, d))

    @classmethod
    def encrypt(cls, pub_key, plainString):
        """Encrypts a string

        Args:
            cls (class attribute): Access a class atribute through keyword cls
            pub_key: Public Key of Elgamal
            plainString: string to be encrypted

        Returns:
            str: a string of the encrypted cipher string
        """
        n, e = pub_key

        cipherArray = []
        # Start Timer
        start_time = time()
        for i, v in enumerate(plainString):
            val = pow(ord(v), e, n)
            cipherArray.append(val)
        # End Timer
        end_time = time()
        number_string = '-'.join((map(str, cipherArray)))
        base64_string = encode(number_string)

        return (base64_string, round((end_time - start_time) * 1000, 4))

    @classmethod
    def decrypt(cls, pri_key, cipherFileString):
        """Decrypts a string

        Args:
            cls (class attribute): Access a class atribute through keyword cls
            pri_key: Private Key of Elgamal
            cipherFileString: a string of the cipher text 1

        Returns:
            str: a string of the decrypted text
        """
        base64_string = decode(cipherFileString)
        cipherFileArray = list(map(int, base64_string.split("-")))
        n, d = pri_key
        plain_hex_arr = []
        # Start Timer
        start_time = time()
        for i, v in enumerate(cipherFileArray):
            val = pow(v, d, n)
            plain_hex_arr.append(val)
        end_time = time()
        # End Timer
        plain_hex_string = cls.unifyString(plain_hex_arr)

        return (plain_hex_string, round((end_time - start_time) * 1000, 4))

    @classmethod
    def unifyString(cls, fileArray):
        """Converts an array of number to a string of its respective ascii value

        Args:
            cls (class attribute): Access a class atribute through keyword cls
            fileArray: array of integers

        Returns:
            str: a string consisting of the ascii value of each number in the array
        """
        string = ''
        for i, v in enumerate(fileArray):
            string = string + chr(v)
        return string
