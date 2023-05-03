import re
from collections import deque

alphabet = deque(chr(65 + i) for i in range(26))


def clean_text(ct: str) -> str:
    # Remove all non-alpha
    return re.sub('[^a-zA-Z]+', '', ct).upper()


def generate_array_vigenere_square() -> list:
    vs = []
    slider = deque(alphabet)
    for i in range(26):
        vs.append(list(slider))
        slider.rotate(-1)
    return vs


def encrypt_plaintext_numerical(pt: str, k: str) -> str:
    pt = clean_text(pt)
    k = clean_text(k)
    sol = ""
    for i in range(len(pt)):
        sol += alphabet[(alphabet.index(pt[i]) + alphabet.index(k[i % len(k)])) % 26]
    return sol


def decrypt_ciphertext_numerical(ct: str, k: str) -> str:
    ct = clean_text(ct)
    k = clean_text(k)
    sol = ""
    for i in range(len(ct)):
        sol += alphabet[(alphabet.index(ct[i]) - alphabet.index(k[i % len(k)])) % 26]
    return sol


def encrypt_plaintext_table(pt: str, k: str) -> str:
    pt = clean_text(pt)
    k = clean_text(k)
    vigenere_square = generate_array_vigenere_square()
    sol = ""
    for i in range(len(pt)):
        sol += vigenere_square[alphabet.index(k[i % len(k)])][alphabet.index(pt[i])]
    return sol


def decrypt_ciphertext_table(ct: str, k: str) -> str:
    ct = clean_text(ct)
    k = clean_text(k)
    vigenere_square = generate_array_vigenere_square()
    sol = ""
    for i in range(len(ct)):
        sol += alphabet[list(vigenere_square[alphabet.index(k[i % len(k)])]).index(ct[i])]
    return sol


print("Vigenere Cipher Toolkit -- Version 1.0")
path = int(input("Please input a selection:\n1: Encryption\n2: Decryption\n"))
match path:
    case 1:
        plaintext = clean_text(input("Enter plaintext: "))
        key = input("Enter Key (as a string): ")
        print("Encrypted Plaintext: " + encrypt_plaintext_table(plaintext, key))
    case 2:
        ciphertext = clean_text(input("Enter ciphertext: "))
        key = input("Enter Key (as a string):")
        print("Decrypted Ciphertext: " + decrypt_ciphertext_table(ciphertext, key))
