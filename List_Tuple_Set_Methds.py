#  List of Values::: ARE MUTABLE - CHANGEABLE
courses = ['History', 'Math', 'Physics', "CompSci"]
print(courses)
print(len(courses))  # shows the length of whole list
print(courses[1])  # gives the 1st subject
print(courses[-1])  # last subject in list
# gives item from Starting up to Ending but not including last :: Also called as Slicing
print(courses[1:4])


# List Methods:::

# APPEND if we want to add some item into our courses list
courses.append('Art')
print(courses)

# INSERT method we want to add multiple entire values into our previous existing list we can also use Insert method where we have to
# provide position indexes
courses.insert(1, 'Biology')
print(courses)
# ex2
courses2 = ['Art', 'Education']
courses.insert(1, courses2)
print(courses)

# EXTEND method, which allows us to extend current list by adding new var in it. No need of indexes
courses.extend(courses2)
print(courses)

# REMOVE method to remove items from a list
courses.remove('Math')  # MAth is removed
print(courses)
courses.pop()  # by default it remives last item from LIst
print(courses)
popRetrievedVal = courses.pop  # created Var and assigned and print retrieved value
print(popRetrievedVal)

# REVERSED method to reverse in opposite
letters = ['a', 'b', 'c', 'd', 'e']
letters.reverse()
print(letters)

# SORT the list  sorting in right way
letters2 = ['c', 'a', 'e', 'b', 'f']
letters2.sort()         # also we can use ' letters2.sort(reverse=True) '
print(letters2)
# ex 2
# will assign into var and print it even easier
sorted_letters2 = sorted(letters2)
print(sorted_letters2)


# Index -> returns items rom the list whichever index num its placed
print(letters.index('b'))


# IN  method TRUE/FALSE ::: returns us Boolean result
print('J' in letters)    # should be false

# MIN_MAX_SUM ::::::;
# MIN -> return min num from the list
# MAX -> returns max from the list
# SUM -> returns sum of the list

# JOIN -> used to rewrite our LIST values as Simple String lines
letters3 = ['q', 'c', 'j', 'a', 'e', 'o', 'b', 'f']
lettersStrings = ', '.join(letters3)   # seperated with comma
print(lettersStrings)

# SPLIT reverse of JOIN reverts to regular format as LIST
new_list = lettersStrings.split(', ')
print(new_list)

# TUPLE :::: NON-MUTABLE format same way as LIST but in (   ), except doesn't mutates the list once modified non changeable
tuple = ('q', 'c', 'k', 'a', 'o', 'o', 'b', 'f')
tuple2 = tuple
print(tuple2)
#tuple2[0] = 'A'
print(tuple2)  # should give an error cause in non-mutable TUPLE

# SET -> value doesn't support Duplicates values. Format is same as LIST but in {  }, Note: Changes order of items in each Execution
set_example = {'q', 'c', 'k', 'a', 'o', 'o', 'w', 'w'}
print(set_example)


# Intersection method -> used to retrieve same-matching values from 2 different List
set1_example = {'q', 'c', 'k', 'a', 'e', 'o', 'q', 'w'}
set2_example = {'b', 'd', 't', 'a', 'e', 'o', 'l', 'q'}
# will return only matching leters
print(set1_example.intersection(set2_example))

# DIFFERENCE -> used to retrieve no-matching value from 2 different List
set1_example = {'q', 'c', 'k', 'a', 'e', 'o', 'q', 'w'}
set2_example = {'b', 'd', 't', 'a', 'e', 'o', 'l', 'q'}
# will return only non-matching leters
print(set1_example.difference(set2_example))

# UNION -> used to Unite 2 different Lists, will retrieve information from 2 lists into 1 List, but will not accept Duplictaed-Matching values
set1_example = {'q', 'c', 'k', 'a', 'e', 'o', 'q', 'w'}
set2_example = {'b', 'd', 't', 'a', 'e', 'o', 'l', 'q'}
# will return only non-matching leters
print(set1_example.union(set2_example))
