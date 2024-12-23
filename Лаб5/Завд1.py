import random


def miller_rabin(p, k):
    """
    Алгоритм Міллера-Рабіна для перевірки числа p на простоту.
    Вхідні дані:
    - p: непарне натуральне число > 3
    - k: кількість раундів
    Вихід:
    - результат простоти числа (True або False)
    - імовірність бути простим
    """
    if p % 2 == 0 or p <= 3:
        return False, 0  # Число повинно бути непарним і більше 3

    # Подання p-1 у вигляді 2^s * d (де d - непарне)
    s, d = 0, p - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    # Головний цикл перевірки
    for _ in range(k):
        # Випадковий вибір бази a
        a = random.randint(2, p - 2)

        # Обчислення a^d mod p
        x = pow(a, d, p)  # Ефективно a^d модуль p
        if x == 1 or x == p - 1:
            continue  # Пройшов тест Міллера

        for _ in range(s - 1):
            x = pow(x, 2, p)  # Піднесення x в квадрат mod p
            if x == p - 1:
                break
        else:
            return False, 0  # Число складене

    # Якщо число пройшло усі раунди
    probability = 1 - 1 / (2 ** k)
    return True, probability


# Приклад використання
if __name__ == "__main__":
    p = int(input("Введіть непарне натуральне число p > 3: "))
    k = int(input("Введіть бажану кількість раундів перевірки k: "))

    is_prime, probability = miller_rabin(p, k)

    if is_prime:
        print(f"Число {p} є простим з імовірністю {probability:.4f}")
    else:
        print(f"Число {p} є складеним.")
