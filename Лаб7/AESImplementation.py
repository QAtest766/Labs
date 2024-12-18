# AES-128 implementation
# Python 3.9.6

def aes_multiply(a, b):
    """
    Galois Field multiplication of two bytes
    """
    result = 0
    for i in range(8):
        if b & 0x01:
            result ^= a
        high_bit_set = a & 0x80
        a = (a << 1) & 0xFF
        if high_bit_set:
            a ^= 0x1b
        b >>= 1
    return result


def s_box(byte):
    """
    S-Box transformation based on mathematical transformations.
    """
    # Inverse in GF(2^8)
    if byte == 0:
        inv = 0
    else:
        inv = pow(byte, 254, 0x11b)  # Inverse in GF(2^8)
    # Affine transformation
    s = inv
    for i in range(4):
        inv = (inv >> 1) | ((inv & 1) << 7)
        s ^= inv
    return s ^ 0x63


def sub_bytes(state):
    """
    SubBytes step using AES's mathematical transformations.
    """
    return [[s_box(byte) for byte in row] for row in state]


def shift_rows(state):
    """
    ShiftRows step - shifts rows in the AES state matrix.
    """
    return [
        state[0],
        state[1][1:] + state[1][:1],
        state[2][2:] + state[2][:2],
        state[3][3:] + state[3][:3]
    ]


def mix_columns(state):
    """
    MixColumns step - linear transformation for mixing columns in AES state.
    """

    def mix_column(column):
        return [
            aes_multiply(column[0], 2) ^ aes_multiply(column[1], 3) ^ column[2] ^ column[3],
            column[0] ^ aes_multiply(column[1], 2) ^ aes_multiply(column[2], 3) ^ column[3],
            column[0] ^ column[1] ^ aes_multiply(column[2], 2) ^ aes_multiply(column[3], 3),
            aes_multiply(column[0], 3) ^ column[1] ^ column[2] ^ aes_multiply(column[3], 2)
        ]

    return [mix_column(column) for column in zip(*state)]


def add_round_key(state, round_key):
    """
    AddRoundKey step - XORing AES state with the round key.
    """
    return [[state[row][col] ^ round_key[row][col] for col in range(4)] for row in range(4)]


def key_expansion(key):
    """
    Expand the cipher key into multiple AES round keys.
    """

    def sub_word(word):
        return [s_box(byte) for byte in word]

    def rot_word(word):
        return word[1:] + word[:1]

    w = []
    for i in range(4):
        w.append(key[4 * i: 4 * (i + 1)])

    for i in range(4, 44):
        temp = w[i - 1]
        if i % 4 == 0:
            temp = sub_word(rot_word(temp))
            temp[0] ^= (0x01 << (i // 4 - 1))
        w.append([w[i - 4][j] ^ temp[j] for j in range(4)])

    return [w[4 * i: 4 * (i + 1)] for i in range(11)]


def encrypt_block(plaintext, key):
    """
    Encrypt a single AES 128 block (16 bytes).
    """
    state = [plaintext[i:i + 4] for i in range(0, len(plaintext), 4)]
    round_keys = key_expansion(key)

    # Initial AddRoundKey
    state = add_round_key(state, round_keys[0])

    # Main rounds
    for i in range(1, 10):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, round_keys[i])

    # Final round (no MixColumns)
    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, round_keys[10])

    # Convert state to single list
    return [state[row][col] for col in range(4) for row in range(4)]


def decrypt_block(ciphertext, key):
    """
    Decrypt a single AES 128 block (16 bytes).
    """
    # Reverse order key_expansion
    round_keys = key_expansion(key)[::-1]
    state = [ciphertext[i:i + 4] for i in range(0, len(ciphertext), 4)]

    # Initial AddRoundKey
    state = add_round_key(state, round_keys[0])

    # Main rounds
    for i in range(1, 10):
        state = shift_rows(state)
        state = sub_bytes(state)
        state = add_round_key(state, round_keys[i])
        state = mix_columns(state)

    # Final round (no MixColumns)
    state = shift_rows(state)
    state = sub_bytes(state)
    state = add_round_key(state, round_keys[10])

    # Convert state to single list
    return [state[row][col] for col in range(4) for row in range(4)]


# Testing
if __name__ == "__main__":
    plaintext = [0x32, 0x43, 0xf6, 0xa8, 0x88, 0x5a, 0x30, 0x8d, 0x31, 0x31, 0x98, 0xa2, 0xe0, 0x37, 0x07, 0x34]
    key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0xcf, 0x03, 0x4f, 0x4e, 0x08, 0x1a]

    ciphertext = encrypt_block(plaintext, key)
    print("Ciphertext:", [hex(byte) for byte in ciphertext])

    decrypted = decrypt_block(ciphertext, key)
    print("Decrypted:", [hex(byte) for byte in decrypted])
