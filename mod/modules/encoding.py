import base64


def encode(num_string):
    encoded_number_string = num_string.encode('ascii')
    base64_encoded_number_string = base64.b64encode(encoded_number_string)
    base64_string = str(base64_encoded_number_string, 'ascii')
    return base64_string


def decode(cipher_string):
    decoded_number_string = cipher_string.encode('ascii')
    base64_decoded_number_string = base64.b64decode(decoded_number_string)
    base64_string = str(base64_decoded_number_string, 'ascii')
    return base64_string
