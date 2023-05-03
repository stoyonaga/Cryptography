import matplotlib.pyplot as plt
from collections import Counter
from collections import deque
import re

alphabet = deque(chr(65 + i) for i in range(26))


def clean_text(ct: str) -> str:
    # Remove all non-alpha
    return re.sub('[^a-zA-Z]+', '', ct).upper()


def generate_char_count(ct: str) -> dict:
    return Counter(ct)


def encrypt_plaintext(pt: str, k: int) -> str:
    return "".join(alphabet[(alphabet.index(char) + k) % 26] for char in pt)


def decrypt_ciphertext(ct: str, k: int) -> str:
    return "".join(alphabet[(alphabet.index(char) - k) % 26] for char in ct)


def generate_english_frequency_analysis(ct: str) -> None:
    # Initialize Style
    plt.style.use("seaborn-v0_8")
    # Label Configuration
    plt.title("Frequency Analysis")
    plt.xlabel("Characters")
    plt.ylabel("Relative Frequency (%)")
    # Frequency Analysis of English Language
    analysis = {
        "A": 8.2,
        "B": 1.5,
        "C": 2.8,
        "D": 4.3,
        "E": 13,
        "F": 2.2,
        "G": 2,
        "H": 6.1,
        "I": 7,
        "J": 0.15,
        "K": 0.77,
        "L": 4,
        "M": 2.4,
        "N": 6.7,
        "O": 7.5,
        "P": 1.9,
        "Q": 0.095,
        "R": 6,
        "S": 6.3,
        "T": 9.1,
        "U": 2.8,
        "V": 0.98,
        "W": 2.4,
        "X": 0.15,
        "Y": 2,
        "Z": 0.074
    }
    # Plot Frequency Analysis of English Alphabet (In Text)
    plt.bar(analysis.keys(), analysis.values(), label="English Language", alpha=0.5)
    cipher_analysis = generate_char_count(ct)
    plt.bar(cipher_analysis.keys(), cipher_analysis.values(), label="Ciphertext", alpha=0.8)
    # Add Legends
    plt.legend(loc="upper right")
    # Plot Frequency Analysis of English Alphabet Against Ciphertext
    plt.show()


def smart_cracker(ct: str) -> None:
    character_candidates = sorted(generate_char_count(ct).keys())
    key_candidates = []
    frequent = ["E", "T", "O", "A", "N"]
    for char1 in frequent:
        for char2 in character_candidates:
            candidate = alphabet[(max(ord(char1) - ord(char2), ord(char2) - ord(char1)))]
            if candidate not in key_candidates:
                print("Key Candidate {} will produce the plaintext: {}".format(candidate,
                                                                               decrypt_ciphertext(clean_text(ct),
                                                                                                  alphabet.index
                                                                                                            (candidate))
                                                                               ))
            key_candidates.append(candidate)


def brute_force(ct: str) -> None:
    print("----- Brute Force -----")
    for i in range(26):
        print("Key {}: {}".format(chr(65 + i), decrypt_ciphertext(ct, alphabet.index(chr(65 + i)))))


print("Caesar Cipher Toolkit -- Version 1.0")
path = int(input("Please input a selection:\n1: Encryption\n2: Decryption\n3: Frequency Analysis of Ciphertext"
                 "\n4: Key Cracker\n"))
match path:
    case 1:
        plaintext = clean_text(input("Enter plaintext: "))
        key = alphabet.index(input("Enter Key (as a character): ").upper())
        print("Encrypted Plaintext: " + encrypt_plaintext(plaintext, key))
    case 2:
        ciphertext = clean_text(input("Enter ciphertext: "))
        key = alphabet.index(input("Enter Key (as a character):").upper())
        print("Decrypted Ciphertext: " + decrypt_ciphertext(ciphertext, key))
    case 3:
        ciphertext = clean_text(input("Enter ciphertext: "))
        generate_english_frequency_analysis(ciphertext)
    case 4:
        ciphertext = clean_text(input("Enter ciphertext: "))
        brute_force(ciphertext)
