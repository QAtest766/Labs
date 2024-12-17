from sympy import mod_inverse
import random
# Додавання двох точок на еліптичній кривій
def elliptic_add(P, Q, a, p):
    if P == "O":  # Якщо одна з точок є нейтральним елементом
        return Q
    if Q == "O":
        return P
    if P == Q:  # Подвоєння точки
        m = (3 * P[0]**2 + a) * mod_inverse(2 * P[1], p) % p
    elif P[0] == Q[0] and P[1] != Q[1]:  # P + (-P) = O
        return "O"
    else:  # Додавання різних точок
        m = (Q[1] - P[1]) * mod_inverse(Q[0] - P[0], p) % p
    x_r = (m**2 - P[0] - Q[0]) % p
    y_r = (m * (P[0] - x_r) - P[1]) % p
    return (x_r, y_r)
# Множення точки на число
def scalar_mult(k, P, a, p):
    result = "O"
    addend = P
    while k:
        if k & 1:
            result = elliptic_add(result, addend, a, p)
        addend = elliptic_add(addend, addend, a, p)
        k >>= 1
    return result
# Генерація ключів
def generate_keys(G, a, p):
    private_key = random.randint(1, p - 1)  # Випадковий приватний ключ
    public_key = scalar_mult(private_key, G, a, p)  # Публічний ключ
    return private_key, public_key
# Шифрування
def encrypt(M, G, Q, a, p):
    k = random.randint(1, p - 1)  # Випадкове число k
    C1 = scalar_mult(k, G, a, p)  # C1 = k*G
    kQ = scalar_mult(k, Q, a, p)  # k*Q
    C2 = elliptic_add(M, kQ, a, p)  # C2 = M + k*Q
    return C1, C2
# Розшифрування
def decrypt(C1, C2, private_key, a, p):
    dC1 = scalar_mult(private_key, C1, a, p)  # d*C1
    dC1_neg = (dC1[0], -dC1[1] % p)  # Знаходимо -d*C1
    M = elliptic_add(C2, dC1_neg, a, p)  # M = C2 - d*C1
    return M
# Параметри
p = 23
a = 1
b = 1
G = (17, 20)
M = (18, 10)  # Повідомлення у вигляді точки на кривій
# Генерація ключів
private_key, public_key = generate_keys(G, a, p)
print("Приватний ключ:", private_key)
print("Публічний ключ:", public_key)
# Шифрування
C1, C2 = encrypt(M, G, public_key, a, p)
print("Шифр (C1, C2):", C1, C2)
# Розшифрування
decrypted_M = decrypt(C1, C2, private_key, a, p)
print("Розшифроване повідомлення:", decrypted_M)