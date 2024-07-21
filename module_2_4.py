'''Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Используя этот список составьте второй список primes содержащий только простые числа.
А так же третий список not_primes, содержащий все не простые числа.
Выведите списки primes и not_primes на экран(в консоль).'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создайте пустые списки primes и not_primes.

primes = []
not_primes = []

# При помощи цикла for переберите список numbers.

for i in numbers:

    # Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.

    for j in range(2, i + 1):  # проверку остатка от деления числа на единицу опускаем, также исключаем из перебора 0 и 1.
        # print(i)
        # print(j)

        # В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes в зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).

        if i != j and i % j == 0:
            not_primes.append(i)
            break
        elif i % j == 0 and i == j:
            primes.append(i)
            break

print('Primes: ', primes)
print('Not primes: ', not_primes)
