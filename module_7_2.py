# Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи, strings - список строк для записи.
def custom_write(file_name, strings):
    # Функция должна:
    # Записывать в файл file_name все строки из списка strings, каждая на новой строке.
    # Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
    f = open(file_name, 'w', encoding='utf-8')
    st_num = 0
    d = {}
    for i in strings:
        st_num += 1
        d.update({(st_num, f.tell()): i})
        f.write(f'{i}\n')
    f.close()
    return d


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
