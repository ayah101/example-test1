# constructor its a function that gets called at the time of creating of object
class Point:
    # this is CONSTRUCTOR which initialize SELF
    def __init__(self, x, y):   # SELF is referenced to the current object
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
print(point.x)
point.x = 23  # now we're changing it
print(point.x)


# ex 2
class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def talks(self):
        print("Hi I'm " + self.name, self.last_name)


person1 = Person('Ayah', 'Noor')
print(person1.name+' '+person1.last_name)
person2 = Person('John', "Smith")
p = person2.talks()
