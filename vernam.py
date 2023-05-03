import re

alphabet = [chr(65 + i) for i in range(26)]


def clean_text(ct: str) -> str:
    # Remove all non-alpha
    return re.sub('[^a-zA-Z]+', '', ct).upper()


def generate_numerical_key_list(k: str) -> list:
    k = clean_text(k)
    return [alphabet.index(i) for i in k]


def vernam_cipher_numerical_keys(text: str, k1: list, k2: list, mode: str) -> str:
    text = clean_text(text)
    sol = ""
    for i in range(len(text)):
        alphabet_index = alphabet.index(text[i % len(text)])
        key1_index = k1[i % len(k1)]
        key2_index = k2[i % len(k2)]
        if mode == "E":
            sol += alphabet[(alphabet_index + key1_index + key2_index) % 26]
        else:
            sol += alphabet[(alphabet_index - key1_index - key2_index) % 26]
    return sol


def vernam_cipher_alphabetical_keys(text: str, k1: str, k2: str, mode: str) -> str:
    text = clean_text(text)
    k1 = generate_numerical_key_list(k1)
    k2 = generate_numerical_key_list(k2)
    sol = ""
    for i in range(len(text)):
        alphabet_index = alphabet.index(text[i % len(text)])
        key1_index = k1[i % len(k1)]
        key2_index = k2[i % len(k2)]
        if mode == "E":
            sol += alphabet[(alphabet_index + key1_index + key2_index) % 26]
        else:
            sol += alphabet[(alphabet_index - key1_index - key2_index) % 26]
    return sol


print("Vernam Cipher (Two-Tapes) Toolkit -- Version 1.0")
path = int(input("Please input a selection:\n1: Encryption with number list\n2: Decryption with number list\n"
                 "3: Encryption with keyword\n"
                 "4: Decryption with keyword\n"))
match path:
    case 1:
        plaintext = input("Enter plaintext:")
        key1 = list(map(int, input("Enter first key [i.e., as: \"1, 2, 3, 4\"]").replace(",", "").split(" ")))
        key2 = list(map(int, input("Enter second key [i.e., as: \"1, 2, 3, 4\"]").replace(",", "").split(" ")))
        print("Encrypted Text: " + vernam_cipher_numerical_keys(plaintext, key1, key2, "E"))
    case 2:
        ciphertext = input("Enter ciphertext:")
        key1 = list(map(int, input("Enter first key [i.e., as: \"1, 2, 3, 4\"]").replace(",", "").split(" ")))
        key2 = list(map(int, input("Enter second key [i.e., as: \"1, 2, 3, 4\"]").replace(",", "").split(" ")))
        print("Encrypted Text: " + vernam_cipher_numerical_keys(ciphertext, key1, key2, "D"))
    case 3:
        ciphertext = input("Enter plaintext:")
        key1 = clean_text(input("Enter first key as a string:"))
        key2 = clean_text(input("Enter second key as a string:"))
        print("Encrypted Text: " + vernam_cipher_alphabetical_keys(ciphertext, key1, key2, "E"))
    case 4:
        ciphertext = input("Enter ciphertext:")
        key1 = clean_text(input("Enter first key as a string:"))
        key2 = clean_text(input("Enter second key as a string:"))
        print("Encrypted Text: " + vernam_cipher_alphabetical_keys(ciphertext, key1, key2, "A"))
