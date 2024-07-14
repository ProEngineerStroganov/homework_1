''' Работа со словарями:
  - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
Например: Имя(str)-Год рождения(int).
  - Выведите на экран словарь my_dict.'''

my_dict = {'Sergey': 1988, 'Mihail': 1986, 'Anna': 1990}
print(my_dict)

# - Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.

print(my_dict.get('Anna', 'Ошибка ключа!'))
print(my_dict.get('Alena', 'Ошибка ключа!'))

# - Добавьте ещё две произвольные пары того же формата в словарь my_dict.

my_dict.update({'Saha': 1987, 'Oleg': 1999})

# - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.

print(my_dict.pop('Mihail'))

#  - Выведите на экран словарь my_dict.

print(my_dict)

'''3. Работа с множествами:
  - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.'''

my_set = {1, 2, 5, 4, 3, 2, 5, 65, 345, 76, 3, 1, 8, 5, 4}

#  - Выведите на экран множество my_set (должны отобразиться только уникальные значения).

print(my_set)

#  - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.

my_set.update({40, 21})

''' - Удалите один любой элемент из множества my_set.
 - Выведите на экран измененное множество my_set.'''
print(my_set.discard(65))  # Почему функция print не выводит содержимое множества?
print(my_set)
