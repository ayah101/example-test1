
# SET Key+Pair value into LIST and initialize it
student = {'name': 'John', 'age': '25', 'courses': ['Math', 'Comp']}
print(student['name'])
print(student.get('age', 'name'))

# SET the Key & Value and retrieve it
student['phone'] = '236-186-1213'
print(student.get('phone'))


# UPDATE in 1- shot
student.update({'name': 'Ayah', 'age': '26', 'phone': '1231-112-121'})
print(student)

# DEL -> removing key+value from LIST
student2 = {'name': 'Ayah', 'age': '26', 'phone': '1231-112-121'}
del student2['age']
print(student2)

# POP -> remove and get value
student3 = {'name': 'Ayah', 'age': '26', 'phone': '1231-112-121'}
age = student3.pop('age')
print(student3)
print(len(student3))
print(student3.keys())
print(student3.values())
print(student3.items())

# lets loop it thorugh to check all keys to print all KEY+VALUE
for key, value in student3.items():
    print(key, value)
