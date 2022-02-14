try:
    import pyperclip
except ImportError:
    print('Библиотека pyperclip не установлена.\nУстановите её если хотите получить скопированый текст.')

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ!"№;%:?*()_+Ё123456789.,'

print('Программа для шифрования и расшифровки шифра Цезаря. Created ZQRey.\n')

# Спрашиваем пользователя хочет он зашифровать или расшихровать
while True:
    print('Введите что вы хотите сделать: (Ш)ифровка, (Р)азшифровка')
    responce = input('> ').lower()
    if responce.startswith('ш'):
        mode = 'encrypt'
        break
    elif responce.startswith('р'):
        mode = 'decrypt'
        break
    else:
        print('Я вас не понимаю...')

# Просим пользователя ввести ключ шифрования
while True:
    maxKey = len(SYMBOLS) - 1
    print(f'Введите ключ (от 0 до {maxKey})')
    responce = input('> ')
    if not responce.isdecimal():
        print('Я не понимаю вас...')
    elif 0 <= int(responce) <= len(SYMBOLS):
        key = int(responce)
        break

# Просим ввести сообщение для шифрования
print(f'Введите сообщение что бы его {mode}:')
message = input('> ')

# Делаем все буквы большими, как в шифре Цезаря
message = message.upper()

# Для хранения результата
translated = ''

# Процесс
for symbol in message:
    # Получаем сообщение
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)  # получаем число символа
        if mode == 'encrypt':
            num = num + key
        if mode == 'decrypt':
            num = num - key
        # Переходим по кругу если вышли за рамки длины SYMBOLS или 0
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        if num < 0:
            num = num + len(SYMBOLS)
        # Переводим число в символ и записываем его
        translated = translated + SYMBOLS[num]
    else:
        # Просто символ без шифрования
        translated = translated + symbol

# Вывод
print(translated)

try:
    pyperclip.copy(translated)
    print("Сообщение скопировано!")
except:
    pass
