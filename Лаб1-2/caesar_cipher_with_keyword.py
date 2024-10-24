def generate_keyword_alphabet(keyword):
    alphabet = 'абвгґдежзийклмнопрстуфхцчшщьюя'
    keyword_unique = ''.join(sorted(set(keyword), key=keyword.index))
    shifted_alphabet = keyword_unique + ''.join([ch for ch in alphabet if ch not in keyword_unique])
    return shifted_alphabet


def caesar_cipher_with_keyword(text, keyword, encrypt=True):
    alphabet = 'абвгґдежзийклмнопрстуфхцчшщьюя'
    shifted_alphabet = generate_keyword_alphabet(keyword)

    if not encrypt:
        alphabet, shifted_alphabet = shifted_alphabet, alphabet

    result = []
    for char in text.lower():
        if char in alphabet:
            index = alphabet.index(char)
            result.append(shifted_alphabet[index])
        else:
            result.append(char)  # не алфавітні символи залишаються без змін
    return ''.join(result)


# Приклад використання
keyword = "ключ"
text = "Добрий Вечір"
encrypted_text = caesar_cipher_with_keyword(text, keyword, encrypt=True)
print(f"Зашифрований текст: {encrypted_text}")

decrypted_text = caesar_cipher_with_keyword(encrypted_text, keyword, encrypt=False)
print(f"Розшифрований текст: {decrypted_text}")