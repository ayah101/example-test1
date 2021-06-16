
# Function-Method with Returning Values
# ex1
def hello_func():
    # pass   # we can leave defs without params now, but we have to come back to assign, for that we need to write PASS
    return 'Hello World!!..'


print(hello_func())
print(hello_func())
print(hello_func().upper())
# DRY -> Don't repeat yourself
print(len('test'))


# Function-MEthod with Returning Arguments (str,int)
# ex2
# -> First we need to create Function_method and assign Parameters within our parenthesis : def hello_func2(STR)
def hello_func2(saying_hello):
    return '{} Function.'.format(saying_hello)


print(hello_func2('Hi word'))


def greet_user():
    print('Hello welcome')
    print('HOpe u re good')


print('Start')
greet_user()
print('finish')


# ex3 with 2 - Parameter
def greet_user2(name, last_name):
    print(f'Hi {name} {last_name}')


print('Start')
greet_user
greet_user2('John', 'Smith')
greet_user2('Mary', 'Joseph')
print('finish')


# ex 4 with 3 int arguments
def amazon(price, shipping, discount):
    return price+shipping - discount


result = amazon(50, 5, 3.7)
print(f'This is final price for ur purchase ' + str(result))
