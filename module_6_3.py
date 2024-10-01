# Horse - класс описывающий лошадь. Объект этого класса обладает следующими атрибутами:
class Horse:
    # x_distance = 0 - пройденный путь.
    x_distance = 0

    # sound = 'Frrr' - звук, который издаёт лошадь.
    sound = 'Frrr'

    # И методами:
    # run(self, dx), где dx - изменение дистанции, увеличивает x_distance на dx.
    def run(self, dx):
        self.x_distance += dx


# Eagle - класс описывающий орла. Объект этого класса обладает следующими атрибутами:
class Eagle:
    # y_distance = 0 - высота полёта
    y_distance = 0

    # sound = 'I train, eat, sleep, and repeat' - звук, который издаёт орёл (отсылка)
    sound = 'I train, eat, sleep, and repeat'

    # И методами:
    # fly(self, dy) где dy - изменение дистанции, увеличивает y_distance на dy.
    def fly(self, dy):
        self.y_distance += dy


# Pegasus - класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
# Объект такого класса должен обладать атрибутами классов родителей в порядке наследования.
class Pegasus(Horse, Eagle):

    # Также обладает методами:
    # move(self, dx, dy) - где dx и dy изменения дистанции. В этом методе должны запускаться наследованные методы run и fly соответственно.
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    # get_pos(self) возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же порядке.
    def get_pos(self):
        return (self.x_distance, self.y_distance)

    # voice - который печатает значение унаследованного атрибута sound.
    def voice(self):
        print(Eagle.sound)


print(Pegasus.mro()) # Проверьте, что класс Pegasus наследует атрибуты и методы от классов Horse и Eagle в нужном порядке.
p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()
