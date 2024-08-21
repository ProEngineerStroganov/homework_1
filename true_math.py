'''В true_math создайте функцию divide, которая принимает два параметра first и second. Функция должна возвращать результат деления first на second, но когда в second записан 0 - возвращать бесконечность.
Бесконечность можно импортировать из встроенной библиотеки math (from math import inf)'''

from math import inf


def divide(first, second):
    if second != 0:
        return first / second
    else:
        return inf


def main():
    print(divide(2, 2))
    print(divide(2, 0))


if __name__ == '__main__':
    main()
