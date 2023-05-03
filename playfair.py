import re

number_mapping = {
    "0": "ZERO",
    "1": "ONE",
    "2": "TWO",
    "3": "THREE",
    "4": "FOUR",
    "5": "FIVE",
    "6": "SIX",
    "7": "SEVEN",
    "8": "EIGHT",
    "9": "NINE",
}


def remove_duplicate_two_gram_entries(pt: str) -> list:
    pt_array = list(char for char in pt)
    for i in range(0, len(pt_array) - 2, 2):
        if pt_array[i] == pt_array[i + 1]:
            pt_array.insert(i + 1, "Q")
    if len(pt_array) % 2 != 0:
        pt_array.append("Q")
    return pt_array


def find_position(gram: list, square: list) -> list:
    positions = []
    for entry in gram:
        for i in range(0, len(square)):
            for j in range(0, len(square[0])):
                if entry == square[i][j]:
                    positions.append([i, j])
    return positions


def clean_text_return_two_grams(ct: str) -> list:
    # Remove all non-alpha
    sol = re.sub('[^0-9a-zA-Z]+', '', ct).upper().replace("J", "I")
    for number in number_mapping.keys():
        if number in sol:
            sol = sol.replace(number, number_mapping[number])
    no_duplicates = remove_duplicate_two_gram_entries(sol)
    sol = []
    sol_pointer = 0
    for i in range(len(no_duplicates)//2):
        entry = []
        for j in range(2):
            entry.append(no_duplicates[sol_pointer])
            sol_pointer += 1
        sol.append(entry)
    return sol


def generate_playfair_square(k: str) -> list:
    characters = [char.upper() for char in "".join(dict.fromkeys(k))]
    for i in range(26):
        if chr(65 + i) not in characters:
            characters.append(chr(65 + i))
    characters.remove("J")
    char_pointer = 0
    grid = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(characters[char_pointer])
            char_pointer += 1
        grid.append(row)
    return grid


def encrypt_plaintext(pt: str, k: str) -> str:
    psquare = generate_playfair_square(k)
    two_grams = clean_text_return_two_grams(pt)
    ct = ""

    print("===== Playsquare from {} =====".format(k))
    for line in psquare:
        print(line)

    print("===== Two-Grams =====")
    for entry in two_grams:
        print(entry)
    print("===== Encryption =====")
    for position in two_grams:
        entry = find_position(position, psquare)
        if entry[0][0] == entry[1][0]:
            ct += psquare[entry[0][0]][(entry[0][1] + 1) % 5]
            ct += psquare[entry[1][0]][(entry[1][1] + 1) % 5]
        elif entry[0][1] == entry[1][1]:
            ct += psquare[(entry[0][0] + 1) % 5][entry[0][1]]
            ct += psquare[(entry[1][0] + 1) % 5][entry[1][1]]
        else:
            # Upper Right Triangle
            ct += psquare[entry[0][0]][entry[1][1]]
            ct += psquare[entry[1][0]][entry[0][1]]
    return ct


def decrypt_ciphertext(ct: str, k: str,) -> str:
    psquare = generate_playfair_square(k)
    two_grams = clean_text_return_two_grams(ct)
    pt = ""

    print("===== Encryption =====")
    for position in two_grams:
        entry = find_position(position, psquare)
        if entry[0][0] == entry[1][0]:
            pt += psquare[entry[0][0]][entry[0][1] - 1 % 5]
            pt += psquare[entry[1][0]][entry[1][1] - 1 % 5]
        elif entry[0][1] == entry[1][1]:
            pt += psquare[entry[0][0] - 1 % 5][entry[0][1]]
            pt += psquare[entry[1][0] - 1 % 5][entry[1][1]]
        else:
            # Upper Right Triangle
            print(entry)
            pt += psquare[entry[0][0]][entry[1][1]]
            pt += psquare[entry[1][0]][entry[0][1]]
    return pt.replace("Q", "")


print("Playfair Cipher -- Version 1.0")
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
