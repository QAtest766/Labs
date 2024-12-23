import random
from math import gcd


# Функція перевірки простоти Міллера-Рабіна
def is_prime(n, k=40):
    """
    Перевірка простоти числа за алгоритмом Міллера-Рабіна.
    n - число для перевірки
    k - кількість раундів
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Подання n-1 у вигляді 2^s * d
    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    # Основний цикл перевірки
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # a^d mod n
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


# Функція для генерації великого простого числа
def generate_large_prime(bits):
    """
    Генерація великого простого числа заданої довжини у бітах.
    bits - довжина числа у бітах
    """
    while True:
        number = random.getrandbits(bits) | (1 << bits - 1) | 1  # Забезпечує MSB = 1 і непарність
        if is_prime(number):
            return number


# Розширений алгоритм Евкліда для знаходження оберненого елементу
def extended_gcd(a, b):
    """
    Розширений алгоритм Евкліда для знаходження оберненого елементу
    """
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def modular_inverse(e, phi):
    """Знаходження мультиплікативної оберненої величини"""
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("Взаємно просте число не знайдено!")
    return x % phi


# Генерація ключів RSA
def generate_rsa_keys(bits=1024):
    """
    Генерує публічні і приватні ключі RSA.
    bits - довжина простих чисел p і q у бітах
    """
    # Генерація двох великих простих чисел
    print("Генеруємо прості числа...")
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    while p == q:  # Переконуємося що p і q різні
        q = generate_large_prime(bits)

    # Обчислення модуля n
    n = p * q

    # Обчислюємо значення функції Ейлера
    phi = (p - 1) * (q - 1)

    # Вибираємо публічний ключ e так, щоб gcd(e, phi) = 1
    e = 65537  # Типове значення e
    if gcd(e, phi) != 1:
        e = random.randint(3, phi - 1)
        while gcd(e, phi) != 1:
            e = random.randint(3, phi - 1)

    # Обчислюємо приватний ключ d (обернений до e за модулем phi)
    d = modular_inverse(e, phi)

    return ((e, n), (d, n))


# Шифрування
def encrypt(message, public_key):
    """Шифрування повідомлення"""
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]


# Розшифрування
def decrypt(ciphertext, private_key):
    """Розшифрування повідомлення"""
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])


# Демонстрація роботи RSA
if __name__ == "__main__":
    print("Генеруємо ключі RSA...")
    public_key, private_key = generate_rsa_keys()
    print(f"Публічний ключ: {public_key}")
    print(f"Приватний ключ: {private_key}")

    # Шифрування і розшифрування
    message = input("Введіть повідомлення для шифрування: ")
    ciphertext = encrypt(message, public_key)
    print(f"Зашифроване повідомлення: {ciphertext}")

    decrypted_message = decrypt(ciphertext, private_key)
    print(f"Розшифроване повідомлення: {decrypted_message}")
