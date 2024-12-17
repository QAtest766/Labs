from sympy import mod_inverse
# Функція для додавання двох точок на кривій
def elliptic_add(P, Q, a, p):
    if P == Q:  # Подвоєння точки
        m = (3 * P[0]**2 + a) * mod_inverse(2 * P[1], p) % p
    elif P[0] == Q[0] and P[1] != Q[1]:  # Особливий випадок: P + (-P) = O
        return "O"
    else:  # Додавання двох різних точок
        m = (Q[1] - P[1]) * mod_inverse(Q[0] - P[0], p) % p
    x_r = (m**2 - P[0] - Q[0]) % p
    y_r = (m * (P[0] - x_r) - P[1]) % p
    return (x_r, y_r)
# Функція для обчислення порядку точки G
def find_order_of_point(G, a, p):
    point = G
    order = 1
    while point != "O":
        order += 1
        point = elliptic_add(point, G, a, p)
    return order
# Параметри кривої
a = 1
p = 23
G = (17, 25)
# Знаходження порядку точки G
order = find_order_of_point(G, a, p)
print(f"Порядок точки G: {order}")