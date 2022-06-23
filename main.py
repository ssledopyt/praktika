class Cat:
    say = 'meow'


    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
    def __str__(self):
        return "that cat:" + self.name
    def __repr__(self):
        return "that cat:" + self.name
    def say_your_name(self):
        print("Hi, my name is " + self.name +',', self.__class__.say)


    @classmethod
    def go(cls):
        print("я иду уже", cls.a)


cats = []
alice = Cat('alice', "wh", 19)
gaga = Cat('gaga', "jj", 1451)
cats.append(alice)
cats.append(gaga)
cats[0].color = "not wh"
cats[0].say_your_name()
cats[1].say_your_name()