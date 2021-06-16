import math
from os import rename
import sys

import requests

print(sys.version)
print(sys.executable)

# Strings
# print('Hi my name is Ayah')
# print('*' * 10)
# price=10
# priceOfApple=price


# ### numerical
# print(price)  ## will print 10
# print(priceOfApple) ## will print 10

# booleans
# is_published = True


# Task
# We check in a patient named John Smith
# he is 20 y old and new patient
# full_name  = 'John Smith'
# age = 20
# is_new = True
# print(full_name+type(age))


# Arithmetic Operations  :::::::::::::::::::::::::::::
# print(10+3)
# print(10-3)
# print(10*3)
# print(10/3)
# print(10%3)
# print(10//3)
# print(10**3)

# Agmented Asingment Operators  :::::::::::::::::::::::
# x=10
# x=x+3
# print(x)
# x+=3
# print(x)
# x-=3
# print(x)
# ex1
# z=10+3*2
# print(z) # 16
# ex2
# s=10+3*2**2   # 2*2 = 4*3 =12+10 =22
# print(s) #22

# ex3
# c=(7-2)*3**3 # 7-2= 5  then 3*3*3=27 after all 5*27= 135 final result
# print(c)

# ex4
# a=(2+3) * 10-3  # 5*10= 50-3= 47
# print(a)


# signs
# oranges = 2
# banana = 10
# grapes = 2
# onions = 5
# result = oranges*banana-grapes+onions
# print(result)

# Round Function (Math modules) we have to IMPORT Math
# x=2.9
# print(round(x)) # rounding
#
# x1= -2.9
# print(abs(x1))
#
# x2=2.9
# print(math.ceil(x2))  # rounds in one whole num
#
# x3= 2.9
# print(math.floor(x3)) # rounds in 1num smaller


# If Else Conditions
# if its hot day , Its a hot day Drink plenty of water!! Otherwise if its cold day, Its cold day wear a warm sweater, otherwise its a lovely day

#   ex2
# day = input('which day is today?')
# if day == 'hot':
#     print("Its a hot day Drink plenty of water!!")
# elif day == 'cold':
#     print(" Its cold day wear a warm sweater")
# else:
#     print('Its a lovely day')

# #ex2:
# week = input('Which day is today?')
# if week == 'Monday':
#     print("Today is monday")
#
# elif week== 'Tuesday':
#     print('today is tuesday')
#
# elif week== 'Friday':
#     print("Today is Fun day")
# else:
#     print("Sorry invalid day of the week")

# ex3
# price = 1000000
# has_credit = True
#
#
# if has_credit:
#     down_payment=0.1*price
# else:
#     down_payment=0.2*price
#     print(f"Down payment :  {down_payment}")


# Logical OPreators :::::::::::;OR ::::AND ::::NOT ::::::::::::
# ex 1
# has_high_income=True
# has_good_credit = True
#
# if has_high_income and has_good_credit:
#     print("Eligible for LOAN")

# # ex2
# has_high_income=False
# has_good_credit = True
#
# if has_high_income or has_good_credit:
#     print("Eligible for LOAN")

#  ex 3
# has_criminal_record = False
# has_good_credit = True
#
# if has_good_credit and not has_criminal_record:
#     print("Eligible for LOAN!!!")


# ex 4
# wight= int(input('Weight: '))
# kgOrlb= input("(L)lb or (K)kg: ")
#
# if kgOrlb.upper()=='L':
#     converted =wight* 0.45
#     print(f"You're {converted} kilos")
# else:
#     converted = wight/0.45
#     print(f"You're {converted }pounds")


# While loop condition ::::::
# ex1
# i = 1
# while i<=5:
#     print('*' * i)
#     i=i+1
#     print("done")

# ex 2
# secret_num=9
# guesses_count =0
# guess_limit=3
# while guesses_count < guess_limit:
#   guess = int(input('Guess: '))
#   guesses_count +=1
# if guess == secret_num:
#       print("Yo win the game")
#       break
# else:
#     print("Yp ure fail the guess!!")
#
# # ex 3 Car GAme
# startMsg = '- to start the car'
# stopMsg = ' - stop the car'
# quitMsg = ' - to quite the car'
# command = ""
# started= False
# stopped = False
#
#
# while True:
#     command = input('>help').lower()
#     if command== 'stop':
#         if stopped:
#             print('Car is already stopped!')
#         else:
#             stopped = True
#         print(stopMsg)
#     elif command == 'start':
#         if started:
#             print(' Car is already started!')
#         else:
#             started = True
#         print(startMsg)
#     elif command == 'help':
#      print(startMsg+', '+stopMsg+', '+quitMsg)
#     elif command.lower() == "quit":
#         break
#     else:
#      print("Sorry i dont understand you help msg")


#  FOR LOOP ::::::::: Range Function ::::::::::::::List of obj []:::::::::::;
#  ex1
#  for item in range (5, 10) --> result will be 5,6,7,8,9
#  for item in range (5,10,2) --> result will be 5,7,9 --> will skill 2 nums

# ex 2
# prices = [10,20,30]
# total =0
# for price in prices:
# total+=price
# print(f"Total : {total}")

# ex3 Nested Loop
# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     print("x" * x_count)  # --> 1st solution
# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     output = ""
# for count in range(x_count):
#     output += "x"
# print(output)  # --->2nd solution


# # ex 4    LIST ::::::
# names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
# print(names[2:])
# names[0] = "Jen"  # --->>  // changing 1st Index num NAme into Jen
# print(names)
r = requests.get("https://google.com")
print(r.status_code)
