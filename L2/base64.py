import re

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+",
            "/"]


def b64encode(text):
    bit_str = ""
    base64_str = ""

    for char in text:
        bin_char = bin(ord(char)).lstrip("0b")
        bin_char = (8 - len(bin_char)) * "0" + bin_char
        bit_str += bin_char

    # Split bit into 6 bit string
    brackets = re.findall('(\d{6})', bit_str)

    # Encode the brackets
    for bracket in brackets:
        if bracket == "000000":
            base64_str += "="
        else:
            base64_str += alphabet[int(bracket, 2)]
    return base64_str


def b64decode(word):
    bit_str = ""
    text_str = ""

    for char in word:
        # Ignore character which are not in the alphabet
        if char in alphabet:
            bin_char = bin(alphabet.index(char)).lstrip("0b")
            bin_char = (6 - len(bin_char)) * "0" + bin_char
            bit_str += bin_char

    # 8bit, to encode
    brackets = re.findall('(\d{8})', bit_str)

    # Decode binary to asciii
    for bracket in brackets:
        text_str += chr(int(bracket, 2))
    return text_str


decodedString = input("String to be encoded: ")
print("Base64 encoded string: " + b64encode(decodedString))
encoded = b64encode(decodedString)
print("Base64 decoded string: " + b64decode(encoded))
