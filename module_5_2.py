'''Реализуйте класс House, объекты которого будут создаваться следующим образом:
House('ЖК Эльбрус', 30)
Объект этого класса должен обладать следующими атрибутами:
self.name - имя, self.number_of_floors - кол-во этажей.'''


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    '''Также должен обладать методом go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.
Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".'''

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            print(new_floor)
        else:
            print("Такого этажа не существует")

    # Необходимо дополнить класс House следующими специальными методами:

    # __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
    def __len__(self):
        return self.number_of_floors

    # __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(str(h1))
print(str(h2))

# __len__
print(len(h1))
print(len(h2))
