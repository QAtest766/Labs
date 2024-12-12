def sha1(data):
    # Константи
    H0 = 0x67452301
    H1 = 0xEFCDAB89
    H2 = 0x98BADCFE
    H3 = 0x10325476
    H4 = 0xC3D2E1F0
    # Допоміжні функції
    def left_rotate(value, shift):
        return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF
    # Підготовка даних
    original_byte_len = len(data)
    original_bit_len = original_byte_len * 8
    data += b'\x80'  # Додаємо 1-біт (0x80)
    while (len(data) * 8) % 512 != 448:  # Додаємо нулі до 448 біт
        data += b'\x00'
    data += original_bit_len.to_bytes(8, 'big')  # Додаємо довжину повідомлення (64 біти)
    # Розбиваємо на 512-бітні блоки
    blocks = [data[i:i + 64] for i in range(0, len(data), 64)]
    # Обробка кожного блоку
    for block in blocks:
        # Ініціалізація 80 слів
        W = [int.from_bytes(block[i:i + 4], 'big') for i in range(0, 64, 4)]
        for i in range(16, 80):
            W.append(left_rotate(W[i - 3] ^ W[i - 8] ^ W[i - 14] ^ W[i - 16], 1))
        # Ініціалізація змінних
        A, B, C, D, E = H0, H1, H2, H3, H4
        # Основний цикл
        for i in range(80):
            if 0 <= i <= 19:
                f = (B & C) | (~B & D)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = B ^ C ^ D
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (B & C) | (B & D) | (C & D)
                k = 0x8F1BBCDC
            else:
                f = B ^ C ^ D
                k = 0xCA62C1D6
            temp = (left_rotate(A, 5) + f + E + k + W[i]) & 0xFFFFFFFF
            E = D
            D = C
            C = left_rotate(B, 30)
            B = A
            A = temp
        # Додаємо результат до поточних значень
        H0 = (H0 + A) & 0xFFFFFFFF
        H1 = (H1 + B) & 0xFFFFFFFF
        H2 = (H2 + C) & 0xFFFFFFFF
        H3 = (H3 + D) & 0xFFFFFFFF
        H4 = (H4 + E) & 0xFFFFFFFF
    # Формуємо підсумковий хеш
    return ''.join(f'{x:08x}' for x in (H0, H1, H2, H3, H4))
# Тестування
message = "Hello, cruel world".encode()
hash_result = sha1(message)
print(f"SHA-1 хеш повідомлення: {hash_result}")