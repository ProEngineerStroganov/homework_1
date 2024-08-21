# В fake_math создайте функцию divide, которая принимает два параметра first и second. Функция должна возвращать результат деления first на second, но когда в second записан 0 - возвращать строку 'Ошибка'.
def divide(first, second):
    if second != 0:
        return first / second
    else:
        return 'Ошибка'


def main():
    print(divide(2, 2))
    print(divide(2, 0))


if __name__ == '__main__':
    main()
