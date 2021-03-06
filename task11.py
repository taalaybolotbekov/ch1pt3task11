
lines = 0
words = 0
letters = 0
 
# Функция open() открывает переданный ей файл
# и возвращает объект, итерация по которому
# позволяет последовательно извлекать строки файла.
for line in open('text.txt', 'r'):
    # Была получена очередная строка.
    # Она присваивается переменной line.
    # Счетчик строк следует увеличить на 1.
    lines += 1
 
    # С помощью len определяется количество символов в строке
    # и добавляется к счетчику букв.
    letters += len(line)
 
    # Код ниже считает количество слов в текущей строке.
 
    # Флаг, сигнализирующий нахождение за пределами слова.
    pos = 'out'
 
    # Цикл перебора строки по символам.
    for letter in line:
        # Если очередной символ не пробел, а флаг в значении "вне слова",
        # то значит начинается новое слово.
        if letter != ' ' and pos == 'out':
            # Поэтому надо увеличить счетчик слов на 1,
            words += 1
            # а флаг поменять на значение "внутри слова".
            pos = 'in'
        # Если очередной символ пробел,
        elif letter == ' ':
            # то следует установить флаг в значение "вне слова".
            pos = 'out'
 
# Вывод количеств строк, слов и символов на экран.
print("Lines:", lines)
print("Words:", words)
print("Letters:", letters)