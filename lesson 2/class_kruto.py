class Animal:
    def __init__(self, name, size, tipe):
        self.name = name
        self.size = size
        self.tipe = tipe

    def move(self):
        print(self.name, "moving")

class Cat(Animal):
    def __init__(self, name, size, tipe, color):
        super().__init__(name, size, tipe)
        self.color = color

    def move(self):
        print(self.name, 'walking')


class kit_big(Cat):
    say = 'aaaaaaar'

    def __init__(self, name, size, tipe, color, pride):
        super().__init__(name, size, tipe, color)
        self.pride = pride

    def attack(self, target):
        print(self.name, 'attack', target.name)


alica = Cat(color='wh', name='alica', size='small', tipe='predator')
print(alica.color)
alica.move()
gosha = kit_big(color='bl', name='gosha', size='big', tipe='predatorrr', pride='main')
gosha.attack(alica)