
# Indexes of String as characters single/partially  :::::::::::::::::
course = 'Python for beginners'
print(course[3:20])

name = 'Jennifer'
print(name[1:-1])  # should print only J
name2 = "Ayjeren"
print(name2[1:-1])

# String Concatenation ::::::::::::::::::::::::::::::::::
first = 'JOhn'
last = 'Smith'
message = first+' ['+last+']'
print(message)

firstName = input("What is your fisrt name?")
lastNAme = input("What is ypu last name?")
fullName = "You'r full name is " + firstName+' ['+lastNAme+']'
print(fullName)

# ALSO WE CAN USE FORMATTED STRINGS:
first = "Ayah"
last = "Smith"
message = f'{first} [{last}] is a coder'
print(message)


# Defining the Strings  ::::::::::::::::::::::::::::::::::::::::::
course = 'Python for beginners'
length = len(course)
print(length)
print(course.replace('beginners', 'Absolute beginners'))
print(course)

# indetifying Word if its included in our sentence
print('Python' in course)  # true
msg2 = "Hello evevryone my name is Ayah Noor".upper()
print(msg2)
print(msg2.find('r'))  # finding letter
print(msg2)

# finding word
print(msg2.find('name'))
