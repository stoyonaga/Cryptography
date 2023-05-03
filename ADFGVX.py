import string
import random
import re


def clean_text(ct: str) -> str:
    # Remove all non-alpha
    return re.sub('[^0-9a-zA-Z]+', '', ct).upper()


def generate_key_square() -> list:
    key_square = [
           ["A", "D", "F", "G", "V", "X"],
           ["A"],
           ["D"],
           ["F"],
           ["G"],
           ["V"],
           ["X"]
           ]
    for i in range(1, len(key_square)):
        key_square[i] += random.choices(string.ascii_uppercase + string.digits, k=6)
    return key_square


def generate_key_numerical_permutation(k: int) -> list:
    if k % 2 == 0:
        sol = [i for i in range(1, k + 1)]
        random.shuffle(sol)
        return sol


def generate_plaintext_rectangle(pt: str, n: int) -> list:
    grid = []
    pt = clean_text(pt)
    pt_pointer = 0
    while pt_pointer < len(pt):
        row = []
        for i in range(n // 2):
            if pt_pointer >= len(pt):
                row.append(random.choices(string.ascii_uppercase)[0])
            else:
                row.append(pt[pt_pointer])
            pt_pointer += 1
        grid.append(row)
    return grid


def get_letter_pairs_from_plaintext_rectangle(rect: list, k: list) -> list:
    vector_rectangle = ""
    for i in range(0, len(rect)):
        for j in range(0, len(rect[i])):
            vector_rectangle += rect[i][j]
    adfgvx_mapping = []
    for char in vector_rectangle:
        for i in range(1, len(k)):
            for j in range(1, len(k[i])):
                if k[i][j] == char:
                    adfgvx_mapping.append([k[i][0], k[0][j - 1], char])
    return adfgvx_mapping


def generate_mapping_table(key2: list, mapping: list) -> list:
    grid = [key2]
    counter = 0
    for i in range(len(key2) // 4):
        row = []
        for j in range(len(key2) // 2):
            row.append(mapping[counter][0])
            row.append(mapping[counter][1])
            counter += 1
        grid.append(row)
    return grid


def encrypt_plaintext(pt: str, key1: list, key2: list) -> str:
    ciphertext = ""

    rect = generate_plaintext_rectangle(pt, len(key2))
    coordinates = get_letter_pairs_from_plaintext_rectangle(rect, key1)
    table = generate_mapping_table(key2, coordinates)
    for i in sorted(key2):
        for j in range(1, (len(key2) // 4) + 1):
            ciphertext += table[j][key2.index(i)]
        ciphertext += " "
    return ciphertext


def decrypt_ciphertext(ct: str, key1: list, key2: list) -> str:
    ct = clean_text(ct)
    counter = 1
    ct_pointer = 0

    grid = [key2]
    for i in range(0, len(key2) // 4):
        grid.append(list(key2))

    for i in range(0, len(key2)):
        for j in range(1, (len(key2) // 4) + 1):
            if counter <= len(key2):
                grid[j][grid[0].index(counter)] = ct[ct_pointer]
            ct_pointer += 1
        counter += 1

    row_encryption = ""
    for i in range(1, len(grid)):
        for j in range(0, len(grid[i])):
            row_encryption += grid[i][j]

    adfgvx_map = "ADFGVX"

    pt = ""

    for i in range(0, len(row_encryption) - 1, 2):
        row = int(adfgvx_map.index(row_encryption[i])) + 1
        col = int(adfgvx_map.index(row_encryption[i + 1])) + 1
        pt += key1[row][col]
    return pt


"""
plaintext = "HQ requests front line situation by telegram. -HQ 7th Corp"
key_1 = [
    ["A", "D", "F", "G", "V", "X"],
    ["A", "C", "O", "8", "X", "F", "4"],
    ["D", "M", "K", "3", "A", "Z", "9"],
    ["F", "N", "W", "L", "0", "J", "D"],
    ["G", "5", "S", "I", "Y", "H", "U"],
    ["V", "P", "1", "V", "B", "6", "R"],
    ["X", "E", "Q", "7", "T", "2", "G"]
]

key_2 = [4, 9, 5, 15, 2, 8, 16, 12, 13, 17, 1, 18, 3, 19, 10, 7, 6, 11, 14, 20]

print(encrypt_plaintext(plaintext, key_1, key_2))
print(decrypt_ciphertext(encrypt_plaintext(plaintext, key_1, key_2), key_1, key_2))
"""


plaintext = "holy toledo!"
square = [
    ["A", "D", "F", "G", "V", "X"],
    ["A", "C", "O", "8", "X", "F", "4"],
    ["D", "M", "K", "3", "A", "Z", "9"],
    ["F", "N", "W", "L", "0", "J", "D"],
    ["G", "5", "S", "I", "Y", "H", "U"],
    ["V", "P", "1", "V", "B", "6", "R"],
    ["X", "E", "Q", "7", "T", "2", "G"]
]

vector = generate_key_numerical_permutation(10)

print(encrypt_plaintext(plaintext, square, vector))
print(decrypt_ciphertext(encrypt_plaintext(plaintext, square, vector), square, vector))
