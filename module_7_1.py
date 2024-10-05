from pprint import pprint


# Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.
# Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables') и обладать следующими свойствами:
class Product:
    def __init__(self, name, weight, category):
        # Атрибут name - название продукта (строка).
        self.name = name
        # Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
        self.weight = float(weight)
        # Атрибут category - категория товара (строка).
        self.category = str(category)

    # Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'. Все данные в строке разделены запятой с пробелами.
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


# Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
class Shop:
    # Инкапсулированный атрибут __file_name = 'products.txt'.
    __file_name = ''

    def __init__(self, name):  # Метод добавлен на случай, если потребуется несколько объектов класса Shop.
        self.__file_name = name
        f = open(self.__file_name, 'a')  # Файл создается при создании объекта.
        f.close()

    # Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
    def get_products(self):
        f = open(self.__file_name, 'r')
        return pprint(f.read())

    # Метод add(self, *products), который принимает неограниченное количество объектов класса Product. Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию). Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .
    def add(self, *products):
        for i in products:
            f = open(self.__file_name, 'r')
            if i.name in f.read():
                print(f'{i.name}, {i.weight}, {i.category} уже есть в магазине')
            else:
                f.close()
                f = open(self.__file_name, 'a')
                f.write(f'{i.name}, {i.weight}, {i.category}\n')
                f.close()


s1 = Shop('products.txt')

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')   # Запись не добавляется поскольку есть совпадение по атрибуту name в первой строке.

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
