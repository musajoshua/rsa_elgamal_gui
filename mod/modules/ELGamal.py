# -----------------------------------------------------------
# ELGamal Class that Performs the Generation, Encryption and Decryption of a string
#
# (C) 2020 Musa Joshua Gideon-Bashir, Abuja, Nigeria
# Released under MIT Public License
# email gidijosh@gmail.com
# -----------------------------------------------------------

import random
from time import clock, time
from .encoding import encode, decode


class ELGamal:
    """
    ELGamal Class that Performs the Generation, Encryption and Decryption of a string
    """
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
    def gcd(cls, a, b):
        """finds the gcd of two numbers a and b

        Args:
            cls (class attribute): Access a class atribute through keyword cls
            a: integer a 
            b: integer b 

        Returns:
            int: gcd of the two numbers
        """

        if a < b:
            return cls.gcd(b, a)
        elif a % b == 0:
            return b
        else:
            return cls.gcd(b, a % b)

    @classmethod
    def modInverse(cls, a, m):
        """finds the modular inverse of two numbers a and m

        Args:
            cls (class attribute): Access a class atribute through keyword cls
            a: integer a 
            m: integer m 

        Returns:
            int: the modular inverse of the two numbers
        """
        a = a % m
        for x in range(1, m):
            if ((a * x) % m == 1):
                return x
        return 1

    @classmethod
    def gen_a(cls, p):
        """finds a, a number between 1 and p-2, and is a coprime of p

        Args:
            cls (class attribute): Access a class atribute through keyword cls
            p: integer p 

        Returns:
            int: a
        """
        a = random.randint(1, p-1)
        while cls.gcd(a, p) != 1:
            a = random.randint(1, p-1)
        return a

    @classmethod
    def generate_keys(cls):
        """generates the keys

        Args:
            cls (class attribute): Access a class atribute through keyword cls

        Returns:
            int: p
            int: g
            int: x
            int: y
        """
        p = random.randint(50, 300)
        while cls.if_prime(p) != True:
            p = random.randint(50, 300)
        g = random.randint(50, p - 1)
        x = cls.gen_a(p)
        y = pow(g, x, p)

        return((p, g, y), (p, x))

    @classmethod
    def encrypt(cls, pub_key, plainString):
        """Encrypts a string

        Args:
            cls (class attribute): Access a class atribute through keyword cls
            pub_key: Public Key of Elgamal
            plainString: string to be encrypted

        Returns:
            str: a string of the encrypted cipher string 1
            str: a string of the encrypted cipher string 2
        """
        p, g, y = pub_key

        c1 = []
        c2 = []
        # Start Timer
        start_time = time()
        k = cls.gen_a(p)
        for i, v in enumerate(plainString):
            c1.append(pow(g, k, p))
            val = (pow(y, k) * ord(v)) % p
            c2.append(val)
        # End Timer
        end_time = time()
        cipherString1 = '-'.join((map(str, c1)))
        cipherString2 = '-'.join((map(str, c2)))
        cipher_string1_base64_string = encode(cipherString1)
        cipher_string2_base64_string = encode(cipherString2)
        return ((cipher_string1_base64_string, cipher_string2_base64_string), round((end_time - start_time) * 1000, 4))

    @classmethod
    def decrypt(cls, pri_key, cipherFileString1, cipherFileString2):
        """Decrypts a string

        Args:
            cls (class attribute): Access a class atribute through keyword cls
            pri_key: Private Key of Elgamal
            cipherFileString1: a string of the cipher string 1
            cipherFileString2: a string of the cipher string 2

        Returns:
            str: a string of the decrypted string
        """
        cipher_string1_base64_string = decode(cipherFileString1)
        cipher_string2_base64_string = decode(cipherFileString2)
        cipherFileArray1 = list(
            map(int, cipher_string1_base64_string.split("-")))
        cipherFileArray2 = list(
            map(int, cipher_string2_base64_string.split("-")))
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
