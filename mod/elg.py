from modules.ELGamal import ELGamal
from modules.FileReader import FileReader
from time import time


# pub_key, pri_key = ELGamal.generate_key()
# print(pub_key)
# print(pri_key)

# msg = FileReader.readPlainFile("./test/test.png")
# data/audio/77kb.flac
msg = FileReader.readPlainFile("input/video/data_2.MOV")

pub_key = (103, 97, 41)
pri_key = (103, 94)


(c1, en_msg), time_taken_encrypt = ELGamal.encrypt(pub_key, msg)
print("Time taken to encrypt :", time_taken_encrypt)

# save the two cipher files
FileReader.writeEncryptedFile(en_msg, "enc1.enc")
FileReader.writeEncryptedFile(c1, "enc2.enc")

# # read the two cipher files
en_msg = FileReader.readEncryptedFile("enc1.enc")
c1 = FileReader.readEncryptedFile("enc2.enc")

dr_msg, time_taken_decrypt = ELGamal.decrypt(pri_key, c1, en_msg)
print("Time taken to decrypt :", time_taken_decrypt)
FileReader.writeDecryptedFile(dr_msg)
