def gcd(a, b):
    """Найбільший спільний дільник."""
    while b != 0:
        a, b = b, a % b
    return a


def phi(m):
    """ Обчислення значення функції Ейлера для заданого m.

    Параметри:
    m -- ціле число

    Повертає:
    Значення функції Ейлера для m
    """
    result = m
    p = 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            result -= result // p
        p += 1
    if m > 1:
        result -= result // m
    return result


def mod_exp(base, exp, mod):
    """Піднесення до степеня за модулем."""
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result


def inverse_element_2(a, n):
    """ Знаходження мультиплікативного оберненого елемента a^(-1) по модулю числа n, використовуючи теорему Ейлера.

    Параметри:
    a -- число для якого потрібно знайти обернений елемент
    n -- модуль

    Повертає:
    Мультиплікативний обернений елемент a^(-1) по модулю n або None, якщо він не існує.
    """
    if gcd(a, n) != 1:
        return None  # Обернений елемент не існує, якщо a і n не взаємно прості.

    phi_n = phi(n)
    return mod_exp(a, phi_n - 1, n)


# Тестування на прикладі a = 5 і n = 18
a, n = 5, 18
inv = inverse_element_2(a, n)
if inv is not None:
    print(f'Мультиплікативний обернений елемент для a = {a} по модулю n = {n} дорівнює {inv}')
else:
    print(f'Мультиплікативний обернений елемент для a = {a} по модулю n = {n} не існує')