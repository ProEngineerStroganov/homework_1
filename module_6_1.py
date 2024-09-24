# 2 класса родителя: Animal, Plant# Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное название каждого животного.
class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name
        # У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
        # eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.
        # Метод eat должен работать следующим образом:
        # Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>", меняется атрибут fed на True.

    def eat(self, food):
        if food.edible:
            self.fed = True
            print(f'{self.name} съел {food.name}')
            # Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>", меняется атрибут alive на False.
            # Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.
        else:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')


# Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения
class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


# 4 класса наследника:
# Mammal, Predator для Animal.
# Flower, Fruit для Plant.
class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    # У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
print(a1.name)
print(a1.fed)
print(a1.alive)
print(p1.name)
print(p1.edible)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
