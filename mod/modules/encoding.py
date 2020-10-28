# -----------------------------------------------------------
# Encoding and Decoding Functions that Performs the Encoding and Decoding of a string to ascii
#
# (C) 2020 Musa Joshua Gideon-Bashir, Abuja, Nigeria
# Released under MIT Public License
# email gidijosh@gmail.com
# -----------------------------------------------------------


import base64


def encode(num_string):
    """Endocdes a string of numbers

    Args:
        num_string: String of Numbers to be encoded

    Returns:
        str: an encoded string of alphabets
    """
    encoded_number_string = num_string.encode("ascii")
    base64_encoded_number_string = base64.b64encode(encoded_number_string)
    base64_string = str(base64_encoded_number_string, "ascii")
    return base64_string


def decode(cipher_string):
    """Endocdes a string of numbers

    Args:
        cipher_string: an encoded string of alphabets

    Returns:
        str: an decoded string of numbers
    """
    decoded_number_string = cipher_string.encode("ascii")
    base64_decoded_number_string = base64.b64decode(decoded_number_string)
    base64_string = str(base64_decoded_number_string, "ascii")
    return base64_string
