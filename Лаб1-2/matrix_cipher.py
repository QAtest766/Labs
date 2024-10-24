import numpy as np


def create_matrix(text, row_key, col_key):
    # Створення матриці з тексту з урахуванням ключів
    rows = len(row_key)
    cols = len(col_key)
    total_elements = rows * cols

    # Заповнення або скорочення тексту до необхідного розміру
    if len(text) < total_elements:
        padded_text = text.ljust(total_elements)
    else:
        padded_text = text[:total_elements]

    matrix = np.array(list(padded_text)).reshape((rows, cols))
    return matrix


def permute_matrix(matrix, row_key, col_key):
    # Перестановка рядків та стовпців відповідно до ключів
    row_permuted_matrix = matrix[np.argsort(row_key)]
    fully_permuted_matrix = row_permuted_matrix[:, np.argsort(col_key)]
    return fully_permuted_matrix


def encrypt(text, row_key, col_key):
    matrix = create_matrix(text, row_key, col_key)
    permuted_matrix = permute_matrix(matrix, row_key, col_key)
    return ''.join(permuted_matrix.flatten())


def decrypt(cipher_text, row_key, col_key):
    rows = len(row_key)
    cols = len(col_key)
    total_elements = rows * cols

    # Заповнення або скорочення шифротексту до необхідного розміру
    if len(cipher_text) < total_elements:
        padded_text = cipher_text.ljust(total_elements)
    else:
        padded_text = cipher_text[:total_elements]

    matrix = np.array(list(padded_text)).reshape((rows, cols))

    inv_row_key = np.argsort(np.argsort(row_key))
    inv_col_key = np.argsort(np.argsort(col_key))

    row_permuted_matrix = matrix[:, inv_col_key]
    original_matrix = row_permuted_matrix[inv_row_key, :]
    return ''.join(original_matrix.flatten()).strip()


# Приклад використання
row_key = [3, 1, 2]
col_key = [2, 1, 3]
text = "HELLO ONE"

encrypted = encrypt(text, row_key, col_key)
print(f"Зашифрований текст: {encrypted}")

decrypted = decrypt(encrypted, row_key, col_key)
print(f"Розшифрований текст: {decrypted}")