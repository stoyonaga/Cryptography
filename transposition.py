import re


def clean_text(ct: str) -> str:
    # Remove all non-alpha
    return re.sub('[^a-zA-Z]+', '', ct).upper()


def generate_numerical_key(k: str) -> list:
    num_key = [ord(z) for z in k]
    index = 1
    sol = [i for i in range(len(k))]
    while index < len(k) + 1:
        min_index = num_key.index(min(num_key))
        sol[min_index] = index
        index += 1
        num_key[min_index] = 9999
    return sol


def generate_grid(pt: str, k: str) -> list:
    grid = []
    pt_pointer = 0
    while pt_pointer < len(pt):
        row = []
        for i in range(len(k)):
            if pt_pointer >= len(pt):
                row.append("*")
            else:
                row.append(pt[pt_pointer])
            pt_pointer += 1
        grid.append(row)
    return grid


def encrypt_plaintext(pt: str, k: str) -> str:
    pt = clean_text(pt)
    k = clean_text(k)
    grid = generate_grid(pt, k)
    grid.insert(0, generate_numerical_key(k))
    counter = 1
    sol = ""
    while counter < len(k) + 1:
        for i in range(1, len(grid)):
            sol += grid[i][grid[0].index(counter)]
        counter += 1
    return sol


def decrypt_ciphertext(ct: str, k: str) -> str:
    grid = generate_grid(ct, k)
    grid.insert(0, generate_numerical_key(k))
    ct_pointer = 0
    counter = 1
    for i in range(1, len(k) + 1):
        for j in range(1, len(grid)):
            grid[j][grid[0].index(i)] = ct[ct_pointer]
            ct_pointer += 1
        counter += 1
    return clean_text(str(grid))


print("Complete Rectangular Transposition with Keyword Toolkit -- Version 1.0")
path = int(input("Please input a selection:\n1: Encryption\n2: Decryption\n"))
match path:
    case 1:
        plaintext = clean_text(input("Enter plaintext: "))
        key = input("Enter Key (as a string): ")
        print("Encrypted Plaintext: " + encrypt_plaintext(plaintext, key))
    case 2:
        ciphertext = clean_text(input("Enter ciphertext: "))
        key = input("Enter Key (as a string):")
        print("Decrypted Ciphertext: " + decrypt_ciphertext(ciphertext, key))
