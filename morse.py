import winsound
import time
import re

"""
References:
    - https://en.wikipedia.org/wiki/Morse_code
    - https://www.youtube.com/watch?v=iy8BaMs_JuI
    
    "Each dit or dah within an encoded character is followed by a period of signal absence, called a space, equal to the 
    dit duration. The letters of a word are separated by a space of duration equal to three dits, and words are 
    separated by a space equal to seven dits."
"""

alphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    "/": "",
    " ": "/"
}


def clean_text(s: str) -> str:
    # Remove all non-alpha
    return re.sub('[^a-zA-Z0-9]+', ' ', s).upper()


def tone_length(dit: int) -> dict:
    scale = 0.03
    mapping = {
        ".": int(dit * scale),
        " ": (dit * 3 * scale) / 1000,
        "-": int((dit * 3) * scale),
        "/": ((dit * 7) * scale) / 1000
    }
    return mapping


def encryption(plaintext: str) -> str:
    words = clean_text(plaintext).split(" ")
    ciphertext = ""
    for word in words:
        for letter in word:
            ciphertext += alphabet[letter]
            ciphertext += " "
        ciphertext += "/ "
    return ciphertext


def audio_encryption(ciphertext: str) -> None:
    interval_time = tone_length(1000)
    for word in ciphertext:
        for character in word:
            if character in [".", "-"]:
                winsound.Beep(1000, interval_time[character])
            else:
                time.sleep(interval_time[character])
            time.sleep(interval_time[" "])


def decrypt_ciphertext(ciphertext: str) -> str:
    keys = list(alphabet.keys())
    values = list(alphabet.values())
    plaintext = ""
    for word in ciphertext.split(" "):
        plaintext += keys[values.index(word)]
    return plaintext.replace("/", "").strip()


path = int(input("Please input a selection:\n1: Encryption\n2: Decryption"))
match path:
    case 1:
        pt = input("Enter Plaintext:")
        ct = encryption(pt)
        print("Ciphertext: {}".format(ct))
        audio_encryption(ct)
    case 2:
        ct = input("Enter Ciphertext:")
        pt = decrypt_ciphertext(ct)
        print("Plaintext: {}".format(pt))
