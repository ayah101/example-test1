# BAsic types of PYTHON
# Numbers
# Strings
# booleans
# --+++++++--
# Complex types of PYTHON
# List
# Dictionaries

# Creating Class used o define new Types which can be used inside of the class and also can have attributes
#   ( starts with cap letter PASCAL-Naming Convention)
class Point:
    def move(self):
        print('move')

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()
point2 = Point()
point2.x = 30
print(point2.x)


def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        max = number
        print(max)
