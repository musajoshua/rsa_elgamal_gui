import io
from mod.modules.RSA import RSA
from mod.modules.FileReader import FileReader
from base64 import b64encode
import eel
import binascii

eel.init('web')

# RSA KEY GENERATION
@eel.expose
def rsa_key_gen():
    pu_key, pr_key = RSA.generate_key()
    return (pu_key, pr_key)

# RSA ENCRYPTION
@eel.expose
def rsa_encrypt(public_key, message):
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
    mime = cipher.split(",")[0]
    cipher_data = cipher.split(",")[1]
    n = private_key[0]
    d = private_key[1]
    private_key = (n, d)
    plain, time_taken_decrypt = RSA.decrypt(private_key, cipher_data)
    return (mime + "," + plain, time_taken_decrypt)


eel.start('index.html', size=(1050, 650))
