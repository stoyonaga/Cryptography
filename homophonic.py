import random
from collections import deque
import re
import numpy as np

alphabet = deque(chr(i) for i in range(65, 91))
alphabet.remove("J")

numerals = deque(i for i in range(1, 26))


def clean_text(ct: str) -> str:
    # Remove all non-alpha
    return re.sub('[^a-zA-Z]+', '', ct).upper()


def generate_rectangle(k: str) -> list:
    k = clean_text(k)
    auxiliary_rectangle = [list(alphabet)]
    for char in k:
        tmp = deque(numerals)
        tmp.rotate(alphabet.index(char))
        auxiliary_rectangle.append(np.array(tmp))
    const = 25
    for i in range(2, len(auxiliary_rectangle)):
        auxiliary_rectangle[i] += const
        const += 25
    return auxiliary_rectangle


def encrypt_plaintext(pt: str, k: str) -> str:
    pt = clean_text(pt)
    k = clean_text(k)

    sol = ""
    rect = generate_rectangle(k)
    for char in pt:
        sol += str(rect[random.randint(1, len(rect) - 1)][alphabet.index(char)]) + " "
    return sol


def decrypt_ciphertext(ct: str, k: str) -> str:
    k = clean_text(k)

    sol = ""
    rect = generate_rectangle(k)
    ct = list(map(int, ct.split(" ")))
    print(ct)


    for char in ct:
        for row in range(1, len(rect)):
            if char in rect[row]:
                sol += alphabet[list(rect[row]).index(char)]
    return sol


print("Homophonic Cipher -- Version 1.0")
path = int(input("Please input a selection:\n1: Encryption\n2: Decryption\n"))
match path:
    case 1:
        plaintext = input("Enter plaintext: ")
        key = input("Enter Key (as a string): ")
        print("Encrypted Plaintext: " + encrypt_plaintext(plaintext, key))
    case 2:
        ciphertext = (input("Enter ciphertext: "))
        key = input("Enter Key (as a string):")
        print("Decrypted Ciphertext: " + decrypt_ciphertext(ciphertext, key))
