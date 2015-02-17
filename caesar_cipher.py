__author__ = 'Nikolay Donchev'


def caesar_encrypt(str, n):
    """
    Caesar Cipher Encryption Plain Text
    """
    encrypted_text = ""
    for i in str:
        if i.isalpha():
            if i.isupper():
                caps = True
            else:
                caps = False
            alphabet = ord(i.lower()) + n
            if alphabet > ord('z'):
                alphabet -= 26
            letter = chr(alphabet)
            if caps is True:
                letter = letter.upper()
            encrypted_text += letter
        else:
            encrypted_text += i
    return encrypted_text

print(caesar_encrypt("abc", 1))
print(caesar_encrypt("ABC", 1))
print(caesar_encrypt("abc", 2))
print(caesar_encrypt("aaa", 7))
print(caesar_encrypt("xyz", 1))
print(caesar_encrypt("Yep I done it", 10))
