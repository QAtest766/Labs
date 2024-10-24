import random

# Український алфавіт
alphabet = 'абвгґдежзийклмнопрстуфхцчшщьюя '

# Створення таблиці заміни (гомофонічної)
homophonic_substitution = {
    'а': ['01', '02', '03'],
    'б': ['04', '05'],
    'в': ['06', '07', '08'],
    'г': ['09'],
    'ґ': ['10'],
    'д': ['11', '12'],
    'е': ['13', '14'],
    'ж': ['15'],
    'з': ['16', '17'],
    'и': ['18', '19'],
    'й': ['20'],
    'к': ['21', '22'],
    'л': ['23', '24', '25'],
    'м': ['26', '27'],
    'н': ['28', '29', '30'],
    'о': ['31', '32', '33'],
    'п': ['34', '35'],
    'р': ['36', '37', '38'],
    'с': ['39', '40'],
    'т': ['41', '42', '43'],
    'у': ['44', '45'],
    'ф': ['46'],
    'х': ['47', '48'],
    'ц': ['49'],
    'ч': ['50'],
    'ш': ['51'],
    'щ': ['52'],
    'ь': ['53'],
    'ю': ['54'],
    'я': ['55', '56'],
    ' ': ['57']  # Пробіл
}

# Перевернутий словник для дешифрування
inverse_homophonic_substitution = {v: k for k, values in homophonic_substitution.items() for v in values}


def encrypt(text):
    encrypted_text = []
    for char in text:
        if char in homophonic_substitution:
            encrypted_text.append(random.choice(homophonic_substitution[char]))
        else:
            encrypted_text.append('??')  # Для символів, яких немає в словнику
    return ' '.join(encrypted_text)


def decrypt(cipher):
    decrypted_text = []
    cipher_elements = cipher.split()
    for element in cipher_elements:
        if element in inverse_homophonic_substitution:
            decrypted_text.append(inverse_homophonic_substitution[element])
        else:
            decrypted_text.append('?')  # Для символів, яких немає в словнику
    return ''.join(decrypted_text)


# Приклад використання
text = "добрий день"
encrypted_text = encrypt(text)
print(f"Зашифрований текст: {encrypted_text}")

decrypted_text = decrypt(encrypted_text)
print(f"Розшифрований текст: {decrypted_text}")