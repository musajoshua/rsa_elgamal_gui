import sys
import binascii
import base64
import filetype


class FileReader:
    @staticmethod
    def readPlainFile(plainFile):
        file = open(plainFile, "rb")
        plainFile = file.read()
        file.close()
        plain_hex_val = binascii.hexlify(plainFile)
        return plain_hex_val

    @staticmethod
    def writeDecryptedFile(decFileData):
        decFileData = binascii.unhexlify(decFileData)
        kind = filetype.guess(decFileData)
        if kind is None:
            print('Cannot guess file type!')
            return
        file = open("dec." + kind.extension, "wb")
        file.write(decFileData)
        file.close()

    @staticmethod
    def readEncryptedFile(encFile):
        file = open(encFile, "r")
        encFile = file.read()
        file.close()
        return encFile

    @staticmethod
    def writeEncryptedFile(fileString, fileName):
        file = open(fileName, "w")
        file.write((str(fileString)))
        file.close()
