import random
from sympy import isprime, primitive_root
# Тест Рабіна-Міллера для перевірки простоти
def rabin_miller_test(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    # Представлення n-1 як 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    # Перевірки
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
# Генерація великого простого числа
def generate_large_prime(bits=16):
    while True:
        p = random.getrandbits(bits)
        if p % 2 == 0:  # Пропускаємо парні числа
            continue
        if rabin_miller_test(p):
            return p
# Алгоритм Ель-Гамаля
def elgamal_encrypt_decrypt():
    # Генерація параметрів
    p = generate_large_prime(16)
    g = primitive_root(p)
    # Закритий ключ
    x = random.randint(2, p - 2)
    # Відкритий ключ
    h = pow(g, x, p)
    print(f"Просте число p: {p}")
    print(f"Первісний корінь g: {g}")
    print(f"Закритий ключ x: {x}")
    print(f"Відкритий ключ h: {h}")
    # Шифрування
    message = int(input("Введіть повідомлення для шифрування (число): "))
    if message >= p:
        raise ValueError("Повідомлення має бути меншим за p")
    y = random.randint(2, p - 2)  # Випадковий ключ
    c1 = pow(g, y, p)
    c2 = (message * pow(h, y, p)) % p
    print(f"Зашифроване повідомлення: (c1, c2) = ({c1}, {c2})")
    # Дешифрування
    s = pow(c1, x, p)
    decrypted_message = (c2 * pow(s, p - 2, p)) % p  # Використання оберненого елемента
    print(f"Розшифроване повідомлення: {decrypted_message}")
# Тестування
elgamal_encrypt_decrypt()