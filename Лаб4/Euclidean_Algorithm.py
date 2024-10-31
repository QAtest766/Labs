def gcdex(a, b):
    """ Ітераційний розширений алгоритм Евкліда.

    Параметри:
    a, b -- цілі числа

    Повертає:
    d, x, y -- такі що d = gcd(a, b) і d = ax + by
    """
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


# Тестування на прикладі a = 612, b = 342
a, b = 612, 342
d, x, y = gcdex(a, b)
print(f'Для a = {a}, b = {b}, (d, x, y) = ({d}, {x}, {y})')