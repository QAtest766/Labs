import random
# Тест Рабіна-Міллера для перевірки числа на простоту
def is_prime(n, k=20):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    # Представляємо n-1 як 2^r * d, де d непарне
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    # k ітерацій перевірки
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
# Генерація безпечного простого числа p (p = 2q + 1)
def generate_safe_prime(bits=512):
    while True:
        q = random.getrandbits(bits - 1)
        if is_prime(q):
            p = 2 * q + 1
            if is_prime(p):
                return p
# Перевірка, чи є число g первісним коренем модулю p
def is_primitive_root(g, p):
    if pow(g, 2, p) == 1 or pow(g, (p - 1) // 2, p) == 1:
        return False
    return True
# Вибір первісного кореня g для p
def find_primitive_root(p):
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g
    return None
# Реалізація протоколу Діффі-Хеллмана
def diffie_hellman(p, g):
    # Приватні ключі
    a = random.randint(2, p - 2)
    b = random.randint(2, p - 2)
    # Публічні ключі
    A = pow(g, a, p)
    B = pow(g, b, p)
    # Спільний секрет
    shared_key_a = pow(B, a, p)
    shared_key_b = pow(A, b, p)
    assert shared_key_a == shared_key_b  # Перевірка
    return shared_key_a
# Генерація параметрів
p = generate_safe_prime(128)  # 128 біт для прикладу
g = find_primitive_root(p)
print(f"Safe prime p: {p}")
print(f"Primitive root g: {g}")
# Обмін ключами
shared_key = diffie_hellman(p, g)
print(f"Shared secret key: {shared_key}")