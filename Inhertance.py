class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print('barks')


class Cat(Mammal):
    def mauws(self):
        print('mauws')


class Lion(Mammal):
    def auww(self):
        print("auw")


dog = Dog()
print(dog.bark())

cat = Cat()
print(cat.mauws())

lion = Lion()
print(lion.auww())
