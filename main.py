import random


# Функция для шифрования текста методом Цезаря
def caesar_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')  # Определяем сдвиг для каждой буквы
            encrypted_text += chr((ord(char) - shift + key) % 26 + shift)  # Шифруем букву с учетом ключа
        else:
            encrypted_text += char  # Нешифруемые символы (например, пробелы) остаются без изменений
    return encrypted_text


# Функция для расшифрования текста методом Цезаря
def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)  # Расшифрование осуществляется с отрицательным ключом


# Функция для построения квадрата Виженера
def generate_vigenere_square(alphabet):
    square = [[0] * 26 for _ in range(26)]  # Создаем квадрат размером 26x26
    for i in range(26):
        for j in range(26):
            square[i][j] = alphabet[(i + j) % 26]  # Заполняем квадрат символами из алфавита
    return square


# Функция для шифрования текста методом Виженера
def vigenere_encrypt(text, key, vigenere_square):
    encrypted_text = ""
    key_index = 0
    for char in text:
        if char.isalpha():  # Проверка, является ли символ буквой
            shift = ord('А') if char.isupper() else ord('а')  # Определение сдвига для текущего символа
            key_char = key[key_index % len(key)].upper()  # Получение символа ключа (циклически)
            # Находим индекс строки и столбца для текущего символа и символа ключа в квадрате Виженера
            row_index = (ord(char.upper()) - ord('А')) % 26
            col_index = (ord(key_char) - ord('А')) % 26
            encrypted_char = vigenere_square[row_index][col_index]  # Используем квадрат Виженера для шифрования
            encrypted_text += encrypted_char.upper() if char.isupper() else encrypted_char.lower()  # Сохранение регистра
            key_index += 1  # Увеличение индекса ключа для следующего символа
        else:
            encrypted_text += char  # Сохранение символов, которые не являются буквами
    return encrypted_text


# Функция для расшифрования текста методом Виженера
def vigenere_decrypt(text, key, vigenere_square):
    decrypted_text = ""
    key_index = 0
    for char in text:
        if char.isalpha():  # Проверка, является ли символ буквой
            shift = ord('A') if char.isupper() else ord('a')  # Определение сдвига для текущего символа
            key_char = key[key_index % len(key)]  # Получение символа ключа (циклически)
            key_shift = ord(key_char.upper()) - ord('A')  # Определение сдвига для символа ключа
            for i in range(26):  # Поиск символа в квадрате Виженера
                if vigenere_square[ord(key_char.upper()) - ord('A')][i] == char.upper():  # Проверка совпадения символов
                    decrypted_char = chr(i + shift)  # Дешифровка символа с учетом ключа
                    decrypted_text += decrypted_char.upper() if char.isupper() else decrypted_char.lower()  # Сохранение регистра
                    break
            key_index += 1  # Увеличение индекса ключа для следующего символа
        else:
            decrypted_text += char  # Сохранение символов, которые не являются буквами
    return decrypted_text


# Основная функция программы
def main():
    # Запрос у пользователя выбора режима работы
    mode = input("Выберите режим (1 - Цезарь, 2 - Виженер): ")
    if mode == "1":  # Если выбран режим шифра Цезаря
        #file_name = input("Введите имя файла: ")
        key = int(input("Введите ключ для шифра Цезаря: "))

        # Шифрование текста методом Цезаря
        with open("text", "r") as file:
            original_text = file.read()

        encrypted_text_caesar = caesar_encrypt(original_text, key)
        with open("encC_text", "w") as file:
            file.write(encrypted_text_caesar)

        # Расшифрование текста методом Цезаря
        decrypted_text_caesar = caesar_decrypt(encrypted_text_caesar, key)
        with open("decC_text", "w") as file:
            file.write(decrypted_text_caesar)

        # Вывод первых строк файлов
        with open("text", "r") as file:
            print("Содержимое файла text.txt:")
            print(file.readline().strip())

        with open("encC_text", "r") as file:
            print("Содержимое файла encC_text.txt:")
            print(file.readline().strip())

        with open("decC_text", "r") as file:
            print("Содержимое файла decC_text.txt:")
            print(file.readline().strip())

    elif mode == "2":  # Если выбран режим шифра Виженера
        #file_name = input("Введите имя файла: ")
        key = input("Введите ключ для шифра Виженера: ")
        alphabet_choice = input("Выберите алфавит замены (1 - случайный, 2 - по порядку): ")
        if alphabet_choice == "1":  # Выбор алфавита замены
            alphabet = ''.join(random.sample([chr(i) for i in range(65, 91)], 26))
        elif alphabet_choice == "2":
            alphabet = ''.join([chr(i) for i in range(65, 91)])

        # Построение квадрата Виженера и вывод
        square = generate_vigenere_square(alphabet)
        print("Квадрат Виженера:")
        for row in square:
            print(' '.join(row))

        # Шифрование текста методом Виженера
        with open("text", "r") as file:
            original_text = file.read()

        encrypted_text_vigenere = vigenere_encrypt(original_text, key, square)
        with open("encV_text", "w") as file:
            file.write(encrypted_text_vigenere)

        # Расшифрование текста методом Виженера
        decrypted_text_vigenere = vigenere_decrypt(encrypted_text_vigenere, key, square)
        with open("decV_text", "w") as file:
            file.write(decrypted_text_vigenere)

        # Вывод первых строк файлов
        with open("text", "r") as file:
            print(f"Содержимое файла text.txt:")
            print(file.readline().strip())

        with open("encV_text", "r") as file:
            print(f"Содержимое файла encV_text.txt:")
            print(file.readline().strip())

        with open("decV_text", "r") as file:
            print(f"Содержимое файла decV_text.txt:")
            print(file.readline().strip())

    else:  # Если выбран неверный режим
        print("Неверный режим. Пожалуйста, выберите 1 или 2.")


if __name__ == "__main__":
    main()
#