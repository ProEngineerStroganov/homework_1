'''Организуйте программу:
Создайте переменную my_string и присвойте ей значение строки с произвольным текстом (функция input()).
Вывести количество символов введённого текста'''
my_string = input('Введите текст ')
print('Длина введенной строки: ', len(my_string))
'''Работа с методами строк:
Используя методы строк, выполните следующие действия:'''
# Выведите строку my_string в верхнем регистре.
print(my_string.upper())
# Выведите строку my_string в нижнем регистре.
print(my_string.lower())
# Измените строку my_string, удалив все пробелы.
print(my_string.replace(' ', ''))
# Выведите первый символ строки my_string.
print(my_string[0])
# Выведите последний символ строки my_string.
print(my_string[-1])
