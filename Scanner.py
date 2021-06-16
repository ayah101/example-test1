# Scanner getting data
name = input('What is you name? ')
print('Hi '+name)

name = input('What your name? ')
color = input("what you favorite color?")


# EXAMPLEEEEE 2 ---  ::::::::::::::::::::::::::::::::::
# print(name+ ' likes ' +color+ ' color')
name = input("What is your name?")
last_name = input("What is your last name?")
age = input("What is your age")
city = input("where are you from?")
marriage = input("Wre you married")
phone_number = input("What is you phone number? ")
kids = input('DO YOU HAVE KIDS? ')
print("This girl's name is: "+name+' ,and her last name is: ' +
      last_name+'. She is '+age+' years old ')

if(marriage == 'yes'):
    print(name + ' is married.')
else:
    print(name+" isn't married")
if(kids == 'yes'):
    print(name+' has kid ')
else:
    print(name + "doesn't have kid ")


# Example 3 ::::::::::::::::::::::::::::::::::::
# What you birthyear and - age  from birth year, then print evevrything
birthyear = input('What is your birth year?')
current_year = input('What is current year?')
age = int(current_year)-int(birthyear)
print("You' re " + str(age) + ' years old .')


# Example 4 ::::::::::::::::::::::::::::::
# Ask a user their weight(in pounds), convert it into kg and print on the terminal
# lb = input("What's your weight in lb's? ")
# weight = float(lb)/2.21
# print(weight)
