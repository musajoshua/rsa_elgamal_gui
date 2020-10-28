# -----------------------------------------------------------
# Main Python File
#
# (C) 2020 Musa Joshua Gideon-Bashir, Ilorin, Nigeria
# Released under MIT Public License
# email gidijosh@gmail.com
# -----------------------------------------------------------


import io
from mod.modules.RSA import RSA
from mod.modules.ELGamal import ELGamal
from mod.modules.FileReader import FileReader
from base64 import b64encode
import eel
import binascii

# initialize eel for root directory ./web
eel.init('web')

# RSA KEY GENERATION
@eel.expose
def rsa_key_gen():
    """Generates RSA keys and sends it to the eel GUI

    Returns:
        int: public key
        int: private key
    """
    pu_key, pr_key = RSA.generate_keys()
    return (pu_key, pr_key)

# RSA ENCRYPTION
@eel.expose
def rsa_encrypt(public_key, message):
    """Encrypt message with rsa

    Args:
        public_key: array of n and e
        message: string of message

    Returns:
        str: string of encrypted message
        timestamp: time taken to encrypt
    """
    mime = message.split(",")[0]
    mess_data = message.split(",")[1]
    n = public_key[0]
    e = public_key[1]
    public_key = (n, e)
    cipher, time_taken_encrypt = RSA.encrypt(
        public_key, mess_data)
    return (mime + "," + cipher, time_taken_encrypt)

# RSA DECRYPTION
@eel.expose
def rsa_decrypt(private_key, cipher):
    """Decrypt cipher with rsa

    Args:
        private_key: array of n and d
        cipher: string of message

    Returns:
        str: string of decrypted message
        timestamp: time taken to encrypt
    """
    mime = cipher.split(",")[0]
    cipher_data = cipher.split(",")[1]
    n = private_key[0]
    d = private_key[1]
    private_key = (n, d)
    plain, time_taken_decrypt = RSA.decrypt(private_key, cipher_data)
    return (mime + "," + plain, time_taken_decrypt)

# ELGamal KEY GENERATION
@eel.expose
def elgamal_key_gen():
    """Generates ELGamal keys and sends it to the eel GUI

    Returns:
        int: public key
        int: private key
    """
    pu_key, pr_key = ELGamal.generate_keys()
    return (pu_key, pr_key)

# ELGamal ENCRYPTION
@eel.expose
def elgamal_encrypt(public_key, message):
    """Encrypt message with ELGamal

    Args:
        public_key: array of p, g and y
        message: string of message

    Returns:
        str: string of encrypted message 1
        str: string of encrypted message 2
        timestamp: time taken to encrypt
    """
    mime = message.split(",")[0]
    mess_data = message.split(",")[1]
    p = public_key[0]
    g = public_key[1]
    y = public_key[2]
    public_key = (p, g, y)
    cipher, time_taken_encrypt = ELGamal.encrypt(
        public_key, mess_data)
    cipher_string1, cipher_string2 = cipher
    return (mime + "," + cipher_string1, mime + "," + cipher_string2, time_taken_encrypt)

# ELGamal DECRYPTION
@eel.expose
def elgamal_decrypt(private_key, cipher_string1, cipher_string2):
    """Decrypt message with ELGamal

    Args:
        private_key: array of p and x
        cipher_string1: string of encrypted message 1
        cipher_string2: string of encrypted message 2

    Returns:
        str: string of decrypted message
        timestamp: time taken to encrypt
    """
    mime = cipher_string2.split(",")[0]
    cipher_data1 = cipher_string1.split(",")[1]
    cipher_data2 = cipher_string2.split(",")[1]
    n = private_key[0]
    d = private_key[1]
    private_key = (n, d)
    plain, time_taken_decrypt = ELGamal.decrypt(
        private_key, cipher_data1, cipher_data2)
    return (mime + "," + plain, time_taken_decrypt)


# start eel with index as index.html
eel.start('index.html', size=(1050, 650))
