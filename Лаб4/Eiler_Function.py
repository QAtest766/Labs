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


# Приклад використання
m = 22
print(f'Функція Ейлера для m = {m} дорівнює {phi(m)}')