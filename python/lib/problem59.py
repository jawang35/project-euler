'''
Problem 59 - XOR Decryption

Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange). For
example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key. The advantage
with the XOR function is that using the same encryption key on the cipher
text, restores the plain text; for example, 65 XOR 42 = 107, then
107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and without
both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified
method is to use a password as a key. If the password is shorter than the
message, which is likely, the key is repeated cyclically throughout the
message. The balance for this method is using a sufficiently long password key
for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower
case characters. Using cipher.txt (right click and 'Save Link/Target As...'),
a file containing the encrypted ASCII codes, and the knowledge that the plain
text must contain common English words, decrypt the message and find the sum
of the ASCII values in the original text.
'''

from itertools import cycle
from string import ascii_lowercase
import re
from lib.config import assets_path
from lib.helpers.runtime import print_answer_and_elapsed_time


def xor_decrypt(key, cipher):
    byte_key = [ord(char) for char in key]
    keys_and_codes = (ord(key_char) ^ cipher_code
                      for (key_char, cipher_code) in zip(cycle(key), cipher))
    return ''.join([chr(code) for code in keys_and_codes])


def answer():
    with open('%s/problem59/cipher.txt' % assets_path) as file:
        def parse(line): return [int(n) for n in line.split(',')]
        cipher = [parse(line) for line in file][0]

        for char1 in ascii_lowercase:
            for char2 in ascii_lowercase:
                for char3 in ascii_lowercase:
                    decrypted_text = xor_decrypt(char1 + char2 + char3, cipher)

                    if re.search(r'the', decrypted_text) is not None and \
                       re.search(r'this', decrypted_text) is not None and \
                       re.search(r'that', decrypted_text) is not None and \
                       re.search(r'and', decrypted_text) is not None:
                        return sum(ord(char) for char in decrypted_text)

if __name__ == '__main__':
        print_answer_and_elapsed_time(answer)
