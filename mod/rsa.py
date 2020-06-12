from modules.RSA import RSA
from modules.FileReader import FileReader
# import magic

# pu_key, pr_key = RSA.generate_key()
# print(pu_key)
# print(pr_key)
pu_key = (198131, 5197)
pr_key = (198131, 120013)

# plainString = FileReader.readPlainFile("./test/test.png")
# data/audio/248kb.flac
plainString = FileReader.readPlainFile("input/video/data_2.MOV")

cipherString, time_taken_encrypt = RSA.encrypt(pu_key, plainString)
print("Time taken to encrypt :", time_taken_encrypt)

FileReader.writeEncryptedFile(cipherString, "enc.enc")

cipherString = FileReader.readEncryptedFile("enc.enc")

plainString, time_taken_decrypt = RSA.decrypt(pr_key, cipherString)
print("Time taken to decrypt :", time_taken_decrypt)
FileReader.writeDecryptedFile(plainString)
