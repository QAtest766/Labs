# Таблиця початкової перестановки
INITIAL_PERMUTATION_TABLE = [58, 50, 42, 34, 26, 18, 10, 2,
                             60, 52, 44, 36, 28, 20, 12, 4,
                             62, 54, 46, 38, 30, 22, 14, 6,
                             64, 56, 48, 40, 32, 24, 16, 8,
                             57, 49, 41, 33, 25, 17, 9, 1,
                             59, 51, 43, 35, 27, 19, 11, 3,
                             61, 53, 45, 37, 29, 21, 13, 5,
                             63, 55, 47, 39, 31, 23, 15, 7]

# Таблиця кінцевої перестановки
FINAL_PERMUTATION_TABLE = [40, 8, 48, 16, 56, 24, 64, 32,
                           39, 7, 47, 15, 55, 23, 63, 31,
                           38, 6, 46, 14, 54, 22, 62, 30,
                           37, 5, 45, 13, 53, 21, 61, 29,
                           36, 4, 44, 12, 52, 20, 60, 28,
                           35, 3, 43, 11, 51, 19, 59, 27,
                           34, 2, 42, 10, 50, 18, 58, 26,
                           33, 1, 41, 9, 49, 17, 57, 25]

# Таблиця розширення
EXPANSION_TABLE = [32, 1, 2, 3, 4, 5,
                   4, 5, 6, 7, 8, 9,
                   8, 9, 10, 11, 12, 13,
                   12, 13, 14, 15, 16, 17,
                   16, 17, 18, 19, 20, 21,
                   20, 21, 22, 23, 24, 25,
                   24, 25, 26, 27, 28, 29,
                   28, 29, 30, 31, 32, 1]

# Таблиця перестановок S-контейнерів
SBOX_TABLES = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]

# Таблиця перестановок P
P_PERMUTATION_TABLE = [16, 7, 20, 21,
                       29, 12, 28, 17,
                       1, 15, 23, 26,
                       5, 18, 31, 10,
                       2, 8, 24, 14,
                       32, 27, 3, 9,
                       19, 13, 30, 6,
                       22, 11, 4, 25]

# Таблиця перестановок ключів PC1
PC1_TABLE = [57, 49, 41, 33, 25, 17, 9,
             1, 58, 50, 42, 34, 26, 18,
             10, 2, 59, 51, 43, 35, 27,
             19, 11, 3, 60, 52, 44, 36,
             63, 55, 47, 39, 31, 23, 15,
             7, 62, 54, 46, 38, 30, 22,
             14, 6, 61, 53, 45, 37, 29,
             21, 13, 5, 28, 20, 12, 4]

# Таблиця перестановок ключів PC2
PC2_TABLE = [14, 17, 11, 24, 1, 5,
             3, 28, 15, 6, 21, 10,
             23, 19, 12, 4, 26, 8,
             16, 7, 27, 20, 13, 2,
             41, 52, 31, 37, 47, 55,
             30, 40, 51, 45, 33, 48,
             44, 49, 39, 56, 34, 53,
             46, 42, 50, 36, 29, 32]

# Кількість зрушень для кожного кола
SHIFTS_TABLE = [1, 1, 2, 2, 2, 2, 2, 2,
                1, 2, 2, 2, 2, 2, 2, 1]


# Допоміжні функції
def permute(block, table):
    return [block[x - 1] for x in table]


def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]


def shift_left(key_chunk, shifts):
    return key_chunk[shifts:] + key_chunk[:shifts]


def sbox_substitution(expanded_half_block):
    # Розподіл expanded_half_block на 8 блоків по 6 бітів
    blocks = [expanded_half_block[i:i + 6] for i in range(0, len(expanded_half_block), 6)]
    result = []

    for i, block in enumerate(blocks):
        row = int(f"{block[0]}{block[-1]}", 2)
        col = int(''.join(str(x) for x in block[1:5]), 2)
        value = SBOX_TABLES[i][row][col]
        bin_value = [int(x) for x in f"{value:04b}"]
        result.extend(bin_value)

    return result


# Реалізація алгоритму DES
def des_encrypt(block, keys):
    block = permute(block, INITIAL_PERMUTATION_TABLE)
    left, right = block[:32], block[32:]
    for i in range(16):
        temp_right = permute(xor(expand(right), keys[i]), P_PERMUTATION_TABLE)
        left, right = right, xor(left, temp_right)
    block = permute(right + left, FINAL_PERMUTATION_TABLE)
    return block


def des_decrypt(block, keys):
    block = permute(block, INITIAL_PERMUTATION_TABLE)
    left, right = block[:32], block[32:]
    for i in range(16):
        temp_right = permute(xor(expand(right), keys[15 - i]), P_PERMUTATION_TABLE)
        left, right = right, xor(left, temp_right)
    block = permute(right + left, FINAL_PERMUTATION_TABLE)
    return block


def key_schedule(key):
    key = permute(key, PC1_TABLE)
    left, right = key[:28], key[:28]
    keys = []
    for shift in SHIFTS_TABLE:
        left = shift_left(left, shift)
        right = shift_left(right, shift)
        keys.append(permute(left + right, PC2_TABLE))
    return keys


def expand(half_block):
    return permute(half_block, EXPANSION_TABLE)


# Тестування
def string_to_bit_array(string):
    array = []
    for char in string:
        bin_value = f"{ord(char):08b}"
        array.extend([int(bit) for bit in bin_value])
    return array


def bit_array_to_string(array):
    result = ''
    for i in range(0, len(array), 8):
        byte = array[i:i + 8]
        byte_str = ''.join([str(bit) for bit in byte])
        result += chr(int(byte_str, 2))
    return result


# Приклад використання
key = "testkey!"  # 8 ASCII знаків
data = "sometext"  # 8 ASCII знаків

# Перетворення ключа та даних на бітовий масив
key_bits = string_to_bit_array(key)
data_bits = string_to_bit_array(data)

# Генерація ключів
keys = key_schedule(key_bits)

# Шифрування
encrypted_bits = des_encrypt(data_bits, keys)
encrypted_text = bit_array_to_string(encrypted_bits)

# Розшифрування
decrypted_bits = des_decrypt(encrypted_bits, keys)
decrypted_text = bit_array_to_string(decrypted_bits)

print(f"Original text: {data}")
print(f"Encrypted text: {encrypted_text}")
print(f"Decrypted text: {decrypted_text}")