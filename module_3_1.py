# Создать переменную calls = 0 вне функций.

calls = 0


# Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
# Функция count_calls подсчитывающая вызовы остальных функций.
def count_calls():
    global calls
    calls = calls + 1


# Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


# Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.

def is_contains(string, list_to_search):
    count_calls()
    ans = False
    for i in list_to_search:
        if i.lower() == string.lower():
            return True
        else:
            continue
    return ans

# Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
